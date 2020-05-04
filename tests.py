from z3 import *
from synthesis import solve, Cell, cell

name_rows = Array('name_rows', IntSort(), Cell)
name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('b')))
name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('d')))
name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))

age_rows = Array('age_rows', IntSort(), Cell)
age_rows = Store(age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
age_rows = Store(age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

score_rows = Array('score_rows', IntSort(), Cell)
score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(50.0), False, StringVal('')))
score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(12.5), False, StringVal('')))
score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(12.5), False, StringVal('')))
score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(99.9), False, StringVal('')))
score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(100.0), False, StringVal('')))

input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
input_table = Store(input_table, StringVal('Name'), name_rows)
input_table = Store(input_table, StringVal('Age'), age_rows)
input_table = Store(input_table, StringVal('Score'), score_rows)

input_col_names = ['Name', 'Age', 'Score']
num_input_rows = 5

if __name__ == "__main__":

     # OUTPUT TABLE sum
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 110, RealVal(0), False, StringVal('')))
    # output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    # output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    # output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))


    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Sum'), output_age_rows)
    output_col_names = ['Sum']
    num_output_rows = 1

    print('Test sum 1')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # OUTPUT TABLE sum 2
    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('b')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('b')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('c')))
    input_table_sum_2 = Store(input_table, StringVal('Name'), name_rows)


    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 41, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 45, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))


    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Sum'), output_age_rows)
    output_col_names = ['Sum']
    num_output_rows = 3

    print('Test sum 2')
    solve(input_table_sum_2, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # OUTPUT TABLE count 1
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 5, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Count'), output_age_rows)
    output_col_names = ['Count']
    num_output_rows = 1

    print('Test count 1 - count number of rows')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # OUTPUT TABLE count 2
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 3, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 1, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 1, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Count'), output_age_rows)
    output_col_names = ['Count']
    num_output_rows = 3

    print('Test count 2 - group 3 together by name')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # OUTPUT TABLE 1
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 4, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('b')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('d')))
    output_name_rows = Store(output_name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('a')))

    output_table_1 = Array('output_table_1', StringSort(), ArraySort(IntSort(), Cell))
    output_table_1 = Store(output_table_1, StringVal('Age'), output_age_rows)
    output_table_1 = Store(output_table_1, StringVal('NAME'), output_name_rows)
    output_col_names = ['Age', 'NAME']
    num_output_rows = 5

    print('Test 1 - just select the table')
    solve(input_table, input_col_names, num_input_rows, output_table_1, output_col_names, num_output_rows)


    # OUTPUT TABLE 2
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 1

    print('Test 2 - age 20 only')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 3
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    output_col_names = ['AGE']
    num_output_rows = 2

    print('Test 3 - only 20 and 21')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 4
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(0), False, StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 24, RealVal(0), False, StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 4

    print('Test 4 - not 23')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 5
    output_age_rows = Array('output_age_rows', IntSort(), Cell)

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 0

    print('Test 5 - empty output table')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 6
    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_col_names = []
    num_output_rows = 0

    print('Test 6 - should be unsat')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 7

    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Udit')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Ebru')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Jeremy')))
    input_table_names = Store(input_table, StringVal('Name'), name_rows)



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

    print('Test 7 - select names')
    solve(input_table_names, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


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

    print('Test 8 - exclude Udit')
    solve(input_table_names, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


    # OUTPUT TABLE 9
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Name'), output_name_rows)
    output_col_names = ['Name']
    num_output_rows = 2

    print('Test 9 - only vids and meds')
    solve(input_table_names, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # # OUTPUT TABLE 10
    # output_name_rows = Array('output_name_rows', IntSort(), Cell)
    # output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    # output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(0), False, StringVal('')))
    # output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Name'), output_name_rows)
    # output_table = Store(output_table, StringVal('Age'), output_age_rows)
    # output_col_names = ['Name', 'Age']
    # num_output_rows = 2

    # print('Test 10')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)

    # # OUTPUT TABLE 11
    # output_name_rows = Array('output_name_rows', IntSort(), Cell)
    # output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Medha')))
    # output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), False, StringVal('Vidhart')))
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 23, RealVal(0), False, StringVal('')))
    # output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(0), False, StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Name'), output_name_rows)
    # output_table = Store(output_table, StringVal('Age'), output_age_rows)
    # output_col_names = ['Name', 'Age']
    # num_output_rows = 2

    # print('Test 11')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)


