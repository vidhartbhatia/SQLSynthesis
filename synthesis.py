from z3 import *
from itertools import *

Cell = Datatype('Cell')
Cell.declare('cell', ('type', StringSort()), ('int', IntSort()), ('real', RealSort()), 
                    ('bool', BoolSort()), ('string', StringSort()))
Cell = Cell.create()
cell = Cell.cell
cellType = Cell.type
cellInt = Cell.int
cellReal = Cell.real
cellBool = Cell.bool
cellString = Cell.string

operators = ["=", "!=", "<", ">", "<=", ">="]

def cellEqual(c1, c2):
    return And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2))

def cellNotEqual(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) != cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) != cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) != cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) != cellString(c2)), False))))

def cellLessThan(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) < cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) < cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), False), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) < cellString(c2)), False))))

def cellGreaterThan(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) > cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) > cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), False), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) > cellString(c2)), False))))

def cellLTE(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) <= cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) <= cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), False), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) <= cellString(c2)), False))))

def cellGTE(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) >= cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) >= cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), False), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) >= cellString(c2)), False))))

def satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant):
    return If(where_operator == StringVal("="), cellEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("!="), cellNotEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<"), cellLessThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">"), cellGreaterThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<="), cellLTE(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">="), cellGTE(input_table[where_col_name][r], where_constant), False))))))

def satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing):
    return If(where_clause_missing, True, satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant))

# def cell_value(c):
#     return If(cellType(c) == StringVal('int'), cellInt(c), \
#     If(cellType(c) == StringVal('real'), cellReal(c) , \
#     If(cellType(c) == StringVal('bool'), cellBool(c), \
#     If(cellType(c) == StringVal('string'), cellString(c), 0))))

def cellAdd(c1, c2):
    return  If(cellType(c1) == StringVal('int'), cell(StringVal('int'), cellInt(c1) + cellInt(c2) , RealVal(0), False, StringVal('')) , \
    If(cellType(c1) == StringVal('real'), cell(StringVal('int'), 0 , cellReal(c1) + cellReal(c2), False, StringVal('')) ,  \
    If(cellType(c1) == StringVal('bool'), cell(StringVal('int'), 0 ,RealVal(0), cellBool(c1), StringVal('')) , \
    If(cellType(c1) == StringVal('string'), cell(StringVal('int'), 0 , RealVal(0), False, cellString(c1) + cellString(c2)), cell(cellType(c1), 0, RealVal(0), False, StringVal(''))))))


def solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows):
    solver = Solver()

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

    # GROUP BY unknown(s)
    group_by_col_name = String('group_by_col_name')
    # GROUP BY domain constraints
    solver.add(Or([group_by_col_name == StringVal(input_col_name) for input_col_name in input_col_names]))

    # compute aggregate columns

    # COUNT
    count_rows = Array('count_rows', IntSort(), Cell)

    for r in range(num_input_rows):
        # create the cell to put inside
        count = IntVal(0)
        for i in range(num_input_rows):
            count += If(And(satisfies_where(input_table,r, where_col_name, where_operator, where_constant, where_clause_missing), cellEqual(input_table[group_by_col_name][r],input_table[group_by_col_name][i])),1,0)
        count_rows = Store(count_rows, r, cell(StringVal('int'), count, RealVal(0), False, StringVal('')))

    input_table = Store(input_table, StringVal('COUNT'), count_rows)
    aggregate_col_names = ['COUNT']

     # SUM
    aggregate_column = String('aggregate_column')
    solver.add(Or([aggregate_column == StringVal(input_col_name) for input_col_name in input_col_names]))

    sum_rows = Array('sum_rows', IntSort(), Cell)

    for r in range(num_input_rows):
        sum = cell(cellType(input_table[aggregate_column][0]), 0, RealVal(0), False, StringVal(''))
        for i in range(num_input_rows):
            sum = cellAdd(sum,If(And(satisfies_where(input_table,r, where_col_name, where_operator, where_constant, where_clause_missing), \
                cellEqual(input_table[group_by_col_name][r],input_table[group_by_col_name][i])),input_table[aggregate_column][r], \
                cell(cellType(input_table[aggregate_column][0]), 0, RealVal(0), False, StringVal(''))))
        sum_rows = Store(sum_rows, r, sum)

    input_table = Store(input_table, StringVal('SUM'), sum_rows)
    aggregate_col_names += ['SUM']



    # SELECT unknowns 
    select_col_names = [String(f'select_col_name{i}') for i in range(len(output_col_names))]

    # SELECT domain constraints
    for select_col_name in select_col_names:
        constraints = [select_col_name == StringVal(input_col_name) for input_col_name in input_col_names]
        constraints += [select_col_name == StringVal(aggregate_col_name) for aggregate_col_name in aggregate_col_names]
        solver.add(Or(constraints))
        

        
   
    # row constraints
    # TODO: Optimization
    for r in range(num_input_rows):
        s = Int(f's{r}')
        solver.add(And(s >= 0, s < num_output_rows))
        implication = And([cellEqual(input_table[select_col_names[c]][r], output_table[StringVal(output_col_names[c])][s]) for c in range(len(select_col_names))])
        solver.add(Implies(satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing), implication))
    for s in range(num_output_rows):
        r = Int(f'r{s}')
        solver.add(And(r >= 0, r < num_input_rows))
        solver.add(satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing))
        solver.add(And([cellEqual(input_table[select_col_names[c]][r], output_table[StringVal(output_col_names[c])][s]) for c in range(len(select_col_names))]))

    for i in range(num_input_rows-1):
        for j in range(i+1, num_input_rows):
            solver.add(Int(f'r{i}') != Int(f'r{j}'))

    for i in range(num_output_rows-1):
        for j in range(i+1, num_output_rows):
            solver.add(Int(f's{i}') != Int(f's{j}'))

   
    # print(sat)
    if solver.check() == sat:
        print(solver.model())
        print("Query generated:")
        # Generate query 
        # the SELECT part
        query = "SELECT "
        for i,output_col, in enumerate(output_col_names):
            query += solver.model()[select_col_names[i]] + " AS " + output_col
            if i < len(output_col_names) - 1:
                query += ", "
        query += " FROM input_table"

        # WHERE
        if is_false(solver.model()[where_clause_missing]):
            query += " WHERE "
            query += solver.model()[where_col_name] + " "
            query += solver.model()[where_operator] + " "
            # print(print_cell_value(solver.model()[where_constant]))
            if simplify(cellType(solver.model()[where_constant])) == StringVal("int"):
                query += str((simplify(cellInt(solver.model()[where_constant]))))
            elif simplify(cellType(solver.model()[where_constant])) == StringVal("real"):
                query += str((simplify(cellReal(solver.model()[where_constant]))))
            elif simplify(cellType(solver.model()[where_constant])) == StringVal("bool"):
                query += str((simplify(cellBool(solver.model()[where_constant]))))
            elif simplify(cellType(solver.model()[where_constant])) == StringVal("string"):
                query += str((simplify(cellString(solver.model()[where_constant]))))

        print(simplify(query))
    else:
        print("Unsat")

    

