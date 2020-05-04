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
# operators = ["="]

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
    # return If(where_operator == StringVal("="), cellEqual(input_table[where_col_name][r], where_constant), False)

def satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing):
    return If(where_clause_missing, True, satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant))



def generate_query(output_col_names, result_col_names):

    # the SELECT part
    query = "SELECT "
    for i,output_col, in enumerate(output_col_names):
        query += solver.model()[result_col_names[i]] + " AS " + output_col

    return simplify(query)


if __name__ == '__main__':
    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Udit')))

    age_rows = Array('age_rows', IntSort(), Cell)
    age_rows = Store(age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
    input_table = Store(input_table, StringVal('Name'), name_rows)
    input_table = Store(input_table, StringVal('Age'), age_rows)

    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)

    input_col_names = ['Name', 'Age']
    output_col_names = ['Age']
    num_input_rows = 5
    num_output_rows = 5

    solver = Solver()

    # SELECT unknowns
    select_col_names = [String(f'select_col_name{i}') for i in range(len(output_col_names))]

    # SELECT domain constraints
    for select_col_name in select_col_names:
        solver.add(Or([select_col_name == StringVal(input_col_name) for input_col_name in input_col_names]))

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
        # print(solver.model())
        print("Query generated:")
        print(generate_query(output_col_names, select_col_names))
    else:
        print("Unsat")

    

