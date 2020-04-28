from z3 import *
from itertools import *

if __name__ == '__main__':
    Cell = Datatype('Cell')
    Cell.declare('cell', ('type', StringSort()), ('int', IntSort()), ('real', RealSort()), 
                        ('bool', BoolSort()), ('string', StringSort()))
    Cell = Cell.create()
    cell = Cell.cell
    cellString = Cell.string

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

    table = Array('table', IntSort(), ArraySort(IntSort(), Cell))
    table = Store(table, 0, name_rows)
    table = Store(table, 1, age_rows)

    print(simplify((cellString(table[0][0]))))