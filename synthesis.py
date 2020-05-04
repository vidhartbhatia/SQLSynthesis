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
# operators = ["=", "<="]

def cellEqual(c1, c2):
    return And(And(And(And(cellType(c1) == cellType(c2), cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2))

def cellNotEqual(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) != cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) != cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) != cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) != cellString(c2))))))

def cellLessThan(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) < cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) < cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) < cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) < cellString(c2))))))

def cellGreaterThan(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) > cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) > cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) > cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) > cellString(c2))))))

def cellLTE(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) <= cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) <= cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) <= cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) <= cellString(c2))))))

def cellGTE(c1, c2):
    return If(cellType(c1) == StringVal('int'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) >= cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('real'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) >= cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('bool'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) >= cellBool(c2)), cellString(c1) == cellString(c2)), \
    If(cellType(c1) == StringVal('string'), And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) >= cellString(c2))))))

def satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant):
    return If(where_operator == StringVal("="), cellEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("!="), cellNotEqual(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<"), cellLessThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">"), cellGreaterThan(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal("<="), cellLTE(input_table[where_col_name][r], where_constant), \
    If(where_operator == StringVal(">="), cellGTE(input_table[where_col_name][r], where_constant), False))))))
    # return If(where_operator == StringVal("="), cellEqual(input_table[where_col_name][r], where_constant), If(where_operator == StringVal("<="), cellLTE(input_table[where_col_name][r], where_constant), False))

def satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing):
    return If(where_clause_missing, True, satisfies_where_helper(input_table, r, where_col_name, where_operator, where_constant))

if __name__ == '__main__':
    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Udit')))

    age_rows = Array('age_rows', IntSort(), Cell)
    age_rows = Store(age_rows, 0, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 1, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 2, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 3, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 4, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    input_table = Array('table', StringSort(), ArraySort(IntSort(), Cell))
    input_table = Store(input_table, StringVal('Name'), name_rows)
    input_table = Store(input_table, StringVal('Age'), age_rows)

    print(simplify(StringVal('Medha') == cellString(input_table[StringVal('Name')][0])))

    output_table = Array('table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(input_table, StringVal('Age'), age_rows)

    input_col_names = ['Name', 'Age']
    output_col_names = ['Age']
    num_rows = 5

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
    solver.add(Or([cellEqual(where_constant, cell) for cell in input_table[where_col_name]]))
    
    # TODO: Optimization
    for c in range(len(output_col_names)):
        for r in range(0, num_rows):
            solver.add(satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing))
            s = Int(f's{r}')
            solver.add(And(s >= 0, s < num_rows))
            input_col_name = select_col_names[c]
            output_col_name = StringVal(output_col_names[c])
            solver.add(cellEqual(input_table[input_col_name][r], output_table[output_col_name][s]))
        for s in range(0, num_rows):
            r = Int(f'r{s}')
            solver.add(And(r >= 0, r < num_rows))
            solver.add(satisfies_where(input_table, r, where_col_name, where_operator, where_constant, where_clause_missing))
            input_col_name = select_col_names[c]
            output_col_name = StringVal(output_col_names[c])
            solver.add(cellEqual(input_table[input_col_name][r], output_table[output_col_name][s]))

    sat = solver.check()
    print(sat)
    if sat:
        print(solver.model())
    

    

