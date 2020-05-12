from z3 import *
from itertools import *
import time

# Datatype to represent table cells
Cell = Datatype('Cell')
Cell.declare('cell', ('type', StringSort()), ('int', IntSort()), ('real', RealSort()), ('string', StringSort()))
Cell = Cell.create()
cell = Cell.cell
cellType = Cell.type
cellInt = Cell.int
cellReal = Cell.real
cellString = Cell.string

# Operators supported in WHERE and HAVING cl
operators = ["=", "!=", "<", ">", "<=", ">="]

# cell dataype helper functions
def cellEqual(c1, c2):
    return And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2), cellReal(c1) == cellReal(c2), cellString(c1) == cellString(c2))

def cellNotEqual(c1, c2):
    return Not(cellEqual(c1, c2))

def cellLessThan(c1, c2):
    return And(cellType(c1) == cellType(c2), Or(cellInt(c1) < cellInt(c2), cellReal(c1) < cellReal(c2), cellString(c1) < cellString(c2)))
    
def cellGreaterThan(c1, c2):
    return And(cellType(c1) == cellType(c2), Or(cellInt(c1) > cellInt(c2), cellReal(c1) > cellReal(c2), cellString(c1) > cellString(c2)))

def cellLTE(c1, c2):
    return And(cellType(c1) == cellType(c2), And(cellInt(c1) <= cellInt(c2), cellReal(c1) <= cellReal(c2), cellString(c1) <= cellString(c2)))

def cellGTE(c1, c2):
    return And(cellType(c1) == cellType(c2), And(cellInt(c1) >= cellInt(c2), cellReal(c1) >= cellReal(c2), cellString(c1) >= cellString(c2)))

def satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant):
    return If(where_operator == StringVal("="), cellEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("!="), cellNotEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<"), cellLessThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">"), cellGreaterThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<="), cellLTE(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">="), cellGTE(input_table[where_col_name][r], where_constant), False))))))

def satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing):
    return If(where_clause_missing, True, satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant))

def cellAdd(c1, c2):
    return cell(cellType(c1), cellInt(c1) + cellInt(c2), cellReal(c1) + cellReal(c2), StringVal(''))

def cellIncrement(c1):
    return cell(StringVal('int'), cellInt(c1) + IntVal(1) , cellReal(c1) + RealVal(1), StringVal(''))

def cellMax(c1, c2):
    return If(cellGreaterThan(c1, c2), c1, c2)

def cellMin(c1, c2):
    return If(cellLessThan(c1, c2), c1, c2)

# based on having and group by paramters generate contraints, check SAT and output query if found, else reurn false
def generateSQL(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows, runWithGroupBy, runWithHaving):

    solver = Solver()
    aggregate_col_names = []
    if runWithGroupBy:
        # aggregate columns
        aggregate_col_names = [ 'MAX', 'MIN', 'SUM', 'COUNT', 'AVG' ]
        aggregate_column = String('aggregate_column')
        solver.add(Or([aggregate_column == StringVal(input_col_name) for input_col_name in input_col_names]))

    # SELECT unknowns 
    select_col_names = [String(f'select_col_name{i}') for i in range(len(output_col_names))]

    # SELECT domain constraints
    for select_col_name in select_col_names:
        constraints = [select_col_name == StringVal(input_col_name) for input_col_name in input_col_names]
        constraints += [select_col_name == StringVal(aggregate_col_name) for aggregate_col_name in aggregate_col_names]
        solver.add(Or(constraints))

    # WHERE unknowns
    where_col_name = String('where_col_name')
    where_operator = String('where_operator')
    where_constant = Const('where_constant', Cell)
    where_clause_missing = Bool('where_clause_missing')

    # WHERE domain constraints
    solver.add(Or([where_col_name == StringVal(input_col_name) for input_col_name in input_col_names]))
    solver.add(Or([where_operator == StringVal(operator) for operator in operators]))
    constraint = False
    for r in range(num_input_rows):
        constraint = Or(constraint, cellEqual(where_constant, input_table[where_col_name][r]))
    solver.add(constraint)

    # booleans representing if row r satisfies where predicate
    r_where_bools = [Bool(f'r{i}_satisfies_where') for i in range(num_input_rows)]
    solver.add(And([r_where_bools[r] == satisfies_where(input_table,r, where_col_name, where_operator, where_constant, where_clause_missing) for r in range(num_input_rows)]))

    if runWithGroupBy:
        # add unique and equal cols
        unique_rows = Array('unique_rows', IntSort(), Cell)
        equal_rows = Array('equal_rows', IntSort(), Cell)
        for i in range(num_input_rows):
            unique_rows = Store(unique_rows, i, cell(StringVal('int'), i, RealVal(0), StringVal('')))
            equal_rows = Store(equal_rows, i, cell(StringVal('int'), 0, RealVal(0), StringVal('')))

        input_table = Store(input_table, StringVal('unique_rows'), unique_rows)
        input_table = Store(input_table, StringVal('equal_rows'), equal_rows)
        group_by_column_names = ['unique_rows', 'equal_rows']

        # GROUP BY unknown(s)
        group_by_col_name = String('group_by_col_name')

        # GROUP BY domain constraints
        g_constraints = [group_by_col_name == StringVal(input_col_name) for input_col_name in input_col_names]
        g_constraints += [group_by_col_name == StringVal(c) for c in group_by_column_names]
        solver.add(Or(g_constraints))

        # Generate aggregate columns as constraints

        # SUM
        sum_rows = Array('sum_rows', IntSort(), Cell)

        default_cell = cell(cellType(input_table[aggregate_column][0]), 0, RealVal(0), StringVal(''))
        for r in range(num_input_rows):
            sump = default_cell
            for i in range(num_input_rows):
                sump = cellAdd(sump, If(And(r_where_bools[r], r_where_bools[i], cellEqual(input_table[group_by_col_name][r], input_table[group_by_col_name][i])), \
                    input_table[aggregate_column][i], default_cell))
            sum_rows = Store(sum_rows, r, sump)

        input_table = Store(input_table, StringVal('SUM'), sum_rows)

        # COUNT
        count_rows = Array('count_rows', IntSort(), Cell)

        for r in range(num_input_rows):
            count = cell(StringVal('int'), 0, RealVal(0), StringVal(''))
            for i in range(num_input_rows):
                count = If(And(And(r_where_bools[r], r_where_bools[i]), cellEqual(input_table[group_by_col_name][r],input_table[group_by_col_name][i])), cellIncrement(count), count)
            count_rows = Store(count_rows, r, count)

        input_table = Store(input_table, StringVal('COUNT'), count_rows)


        # AVG
        avg_rows = Array('avg_rows', IntSort(), Cell)

        for r in range(num_input_rows):
            # sum_cell = input_table[StringVal('SUM')][r]
            # sum_type = cellType(sum_cell)
            # avg = If(sum_type == StringVal('int'), cellInt(sum_cell), If(sum_type == StringVal('real'), cellReal(sum_cell), RealVal(0))) / cellInt(input_table[StringVal('COUNT')][r])
            # avg = cellReal(input_table[StringVal('SUM')][r]) / cellReal(input_table[StringVal('COUNT')][r])
            
            # avg = If(count_real == RealVal(0), RealVal(0), If(sum_type == StringVal('int'), cellInt(sum_cell), If(sum_type == StringVal('real'), cellReal(sum_cell), 0)) / count_real)
            
            # count = cellInt(input_table[StringVal('COUNT')][r])
            # avg = If(count == 0, RealVal(0), cellInt(sum_cell) / count)

            # count_real = cellReal(input_table[StringVal('COUNT')][r])
            # count_real = cellReal(count_rows[r])
            # avg = If(count_real == RealVal(0), RealVal(0), cellReal(sum_rows[r]) / count_real)
            # count_real = cellReal(count_rows[r])
            # solver.add(Not(count_real == RealVal(0)))
            
            # TODO fix hardcoded 5
            avg_rows = Store(avg_rows, r, cell(StringVal('real'), 0, cellReal(sum_rows[r]) / RealVal(5), StringVal('')))
        
        input_table = Store(input_table, StringVal('AVG'), avg_rows)

        
        # MAX
        max_rows = Array('max_rows', IntSort(), Cell)

        for r in range(num_input_rows):
            max_val = input_table[aggregate_column][r]
            for i in range(num_input_rows):
                max_val = cellMax(max_val, If(And(And(r_where_bools[r], r_where_bools[i]), cellEqual(input_table[group_by_col_name][r], input_table[group_by_col_name][i])), \
                    input_table[aggregate_column][i], max_val))
            max_rows = Store(max_rows, r, max_val)
        
        input_table = Store(input_table, StringVal('MAX'), max_rows)


        # MIN
        min_rows = Array('min_rows', IntSort(), Cell)

        for r in range(num_input_rows):
            min_val = input_table[aggregate_column][r]
            for i in range(num_input_rows):
                min_val = cellMin(min_val, If(And(And(r_where_bools[r], r_where_bools[i]), cellEqual(input_table[group_by_col_name][r], input_table[group_by_col_name][i])), \
                    input_table[aggregate_column][i], min_val))
            min_rows = Store(min_rows, r, min_val)
        
        input_table = Store(input_table, StringVal('MIN'), min_rows)

    if runWithHaving:
        # HAVING unknowns
        having_col_name = String('having_col_name')
        having_operator = String('having_operator')
        having_constant = Const('having_constant', Cell)
        having_clause_missing = Bool('having_clause_missing')

        # HAVING domain constraints
        solver.add(Or(having_clause_missing, And(Or([having_col_name == StringVal(aggregate_col_name) for aggregate_col_name in aggregate_col_names]), \
            Or([having_col_name == select_col_name for select_col_name in select_col_names]))))
        solver.add(Or([having_operator == StringVal(operator) for operator in operators]))
        constraint = False
        for r in range(num_input_rows):
            constraint = Or(constraint, cellEqual(having_constant, input_table[having_col_name][r]))
        solver.add(constraint)

        # booleans representing if row r satisfies HAVING predicate
        r_having_bools = [Bool(f'r{i}_satisfies_having') for i in range(num_input_rows)]
        solver.add(And([r_having_bools[r] == satisfies_where(input_table, r, having_col_name, having_operator, having_constant, having_clause_missing) for r in range(num_input_rows)]))

    # row constraints
    # TODO: Optimization
    s_vars = []
    r_vars = []
    for r in range(num_input_rows):
        s = Int(f's{r}')
        s_vars.append(s)
        solver.add(And(s >= 0, s < num_output_rows))
        cells_equal = And([cellEqual(input_table[select_col_names[c]][r], output_table[StringVal(output_col_names[c])][s]) for c in range(len(select_col_names))])
        if runWithHaving:
            solver.add(Implies(And(r_where_bools[r], r_having_bools[r]), cells_equal))
        else:
            solver.add(Implies(r_where_bools[r], cells_equal))

    for s in range(num_output_rows):
        r = Int(f'r{s}')
        r_vars.append(r)
        solver.add(And(r >= 0, r < num_input_rows))
        cells_equal = And([cellEqual(input_table[select_col_names[c]][r], output_table[StringVal(output_col_names[c])][s]) for c in range(len(select_col_names))])
        solver.add(satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing))
        if runWithHaving:
            solver.add(satisfies_where(input_table, r, having_col_name, having_operator, having_constant, having_clause_missing))
        solver.add(cells_equal)

    if runWithGroupBy and runWithHaving:
        for i in range(num_input_rows-1):
            for j in range(i+1, num_input_rows):
                    solver.add(Implies(And(r_where_bools[i] , r_where_bools[j], r_having_bools[i], r_having_bools[j], cellNotEqual(input_table[group_by_col_name][i],input_table[group_by_col_name][j])), s_vars[i] != s_vars[j]))
    elif runWithGroupBy:
        for i in range(num_input_rows-1):
            for j in range(i+1, num_input_rows):
                if (i!=j):
                    solver.add(Implies(And(r_where_bools[i] , r_where_bools[j], cellNotEqual(input_table[group_by_col_name][i],input_table[group_by_col_name][j])), s_vars[i] != s_vars[j]))
    else:
        for i in range(num_input_rows-1):
            for j in range(i+1, num_input_rows):
                if (i!=j):
                    solver.add(Implies(And(r_where_bools[i], r_where_bools[j]), s_vars[i] != s_vars[j]))

    for i in range(num_output_rows):
        for j in range(num_output_rows):
            if (i!=j):
                solver.add(r_vars[i] != r_vars[j])
    
    if solver.check() == sat:
        # print((solver.model().eval(simplify(input_table[StringVal("AVG")]))))
        print("Query generated:")
        # print(solver)
        # print(solver.model())
        # Generate query 
        # the SELECT part
        b = False
        query = "SELECT "
        for i,output_col, in enumerate(output_col_names):
            col_name = solver.model()[select_col_names[i]]
            query += col_name
            if col_name == StringVal("COUNT") or col_name == StringVal("SUM") or col_name == StringVal("AVG") or col_name == StringVal("MAX") or col_name == StringVal("MIN") :
                b = True
                query += "(" + solver.model()[aggregate_column] + ")"
            query += " AS " + output_col
            if i < len(output_col_names) - 1:
                query += ", "
        query += " FROM input_table"

        # WHERE
        if is_false(solver.model()[where_clause_missing]):
            query += " WHERE "
            query += solver.model()[where_col_name] + " "
            query += solver.model()[where_operator] + " "
            if simplify(cellType(solver.model()[where_constant])) == StringVal("int"):
                query += str((simplify(cellInt(solver.model()[where_constant]))))
            elif simplify(cellType(solver.model()[where_constant])) == StringVal("real"):
                query += str((simplify(cellReal(solver.model()[where_constant]))))
            elif simplify(cellType(solver.model()[where_constant])) == StringVal("string"):
                query += str((simplify(cellString(solver.model()[where_constant]))))

        # GROUP BY
        if runWithGroupBy:
            gb_col_name = solver.model()[group_by_col_name]
            if b and not(gb_col_name == StringVal('unique_rows') or gb_col_name == StringVal('equal_rows')):
                query += " GROUP BY " + solver.model()[group_by_col_name]

         # HAVING
        if runWithHaving:
            if b and is_false(solver.model()[having_clause_missing]):
                query += " HAVING "
                query += solver.model()[having_col_name] + "(" + solver.model()[aggregate_column] + ") "
                query += solver.model()[having_operator] + " "
                if simplify(cellType(solver.model()[having_constant])) == StringVal("int"):
                    query += str((simplify(cellInt(solver.model()[having_constant]))))
                elif simplify(cellType(solver.model()[having_constant])) == StringVal("real"):
                    query += str((simplify(cellReal(solver.model()[having_constant]))))
                elif simplify(cellType(solver.model()[having_constant])) == StringVal("string"):
                    query += str((simplify(cellString(solver.model()[having_constant]))))
           
        print(simplify(query))
        return True
    else:
        return False
    

    # print(sat)
def solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows):
    set_param('parallel.enable', True)
    z3.set_param('sat.local_search_threads', 16)
    z3.set_param('sat.threads', 16)
    t1 = time.time()
    if generateSQL(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows, False, False):
        print("without group by, in time %0.2f " % (time.time() - t1))
    elif generateSQL(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows, True, False):
        print("with group by, in time %0.2f" % (time.time() - t1))
    elif generateSQL(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows, True, True):
        print("with having in time %0.2f " % (time.time() - t1))
    else:
        print("Unsat \n")
    

    

