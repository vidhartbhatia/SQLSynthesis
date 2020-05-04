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

def compareCell(c1, c2):
    return And(And(And(And(cellType(c1) == cellType(c2),  cellInt(c1) == cellInt(c2)), cellReal(c1) == cellReal(c2)), cellBool(c1) == cellBool(c2)), cellString(c1) == cellString(c2))







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
    age_rows = Store(age_rows, 0, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 1, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 2, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 3, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    age_rows = Store(age_rows, 4, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    input_table = Array('table', StringSort(), ArraySort(IntSort(), Cell))
    input_table = Store(input_table, StringVal('Name'), name_rows)
    input_table = Store(input_table, StringVal('Age'), age_rows)

    # print(simplify(StringVal('Medha') == cellString(input_table[StringVal('Name')][0])))

    output_table = Array('table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(input_table, StringVal('ages'), age_rows)

    input_col_names = ['Name', 'Age']
    output_col_names = ['ages']
    num_rows = 5

    solver = Solver()

    result_col_names = [String(f'result_col_name{i}') for i in range(len(output_col_names))]

    # SELECT domain constraints
    for result_col_name in result_col_names:
        solver.add(Or([result_col_name == StringVal(input_col_name) for input_col_name in input_col_names]))
    
    # TODO: Optimization
    for c in range(len(output_col_names)):
        for r in range(0, num_rows):
            s = Int(f's{r}')
            solver.add(And(s >= 0, s < num_rows))
            input_col_name = result_col_names[c]
            output_col_name = StringVal(output_col_names[c])
            solver.add(compareCell(input_table[input_col_name][r], output_table[output_col_name][s]))
        for s in range(0, num_rows):
            r = Int(f'r{s}')
            solver.add(And(r >= 0, r < num_rows))
            input_col_name = result_col_names[c]
            output_col_name = StringVal(output_col_names[c])
            solver.add(compareCell(input_table[input_col_name][r], output_table[output_col_name][s]))

    sat = solver.check()
    # print(sat)
    if sat:
        # print(solver.model())
        print("Query generated:")
        print(generate_query(output_col_names, result_col_names))
    else:
        print("Unsat")

    

