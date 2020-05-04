from z3 import *
from synthesis import solve, Cell, cell

name_rows = Array('name_rows', IntSort(), Cell)
name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))
name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Udit')))

age_rows = Array('age_rows', IntSort(), Cell)
age_rows = Store(age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 1, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

score_rows = Array('score_rows', IntSort(), Cell)
score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(50.0), False, StringVal('')))
score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(12.5), False, StringVal('')))
score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(0.5), False, StringVal('')))
score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(99.9), False, StringVal('')))
score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(100.0), False, StringVal('')))

input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
input_table = Store(input_table, StringVal('Name'), name_rows)
input_table = Store(input_table, StringVal('Age'), age_rows)
input_table = Store(input_table, StringVal('Score'), score_rows)

input_col_names = ['Name', 'Age', 'Score']
num_input_rows = 5

if __name__ == "__main__":

    # OUTPUT TABLE 1
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 2, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 1, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 1, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 1, RealVal(0), False, StringVal('')))


    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Count'), output_age_rows)
    output_col_names = ['Count']
    num_output_rows = 4

    print('Test 1')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)



    # OUTPUT TABLE 1
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 5

    print('Test 1')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 2
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 1

    print('Test 2')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 3
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    output_col_names = ['AGE']
    num_output_rows = 2

    print('Test 3')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 4
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 4

    print('Test 4')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 5
    output_age_rows = Array('output_age_rows', IntSort(), Cell)

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 0

    print('Test 5')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 6
    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_col_names = []
    num_output_rows = 0

    print('Test 6')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 7
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))
    output_name_rows = Store(output_name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Udit')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    output_col_names = ['NAME']
    num_output_rows = 5

    print('Test 7')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 8
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    output_col_names = ['NAME']
    num_output_rows = 4

    print('Test 8')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 9
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Name'), output_name_rows)
    output_col_names = ['Name']
    num_output_rows = 2

    print('Test 9')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


