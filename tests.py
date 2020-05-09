from z3 import *
from synthesis import solve, Cell, cell

name_rows = Array('name_rows', IntSort(), Cell)
name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))
name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))

age_rows = Array('age_rows', IntSort(), Cell)
age_rows = Store(age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
age_rows = Store(age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
age_rows = Store(age_rows, 2, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
age_rows = Store(age_rows, 3, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
age_rows = Store(age_rows, 4, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

score_rows = Array('score_rows', IntSort(), Cell)
score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(12.5), StringVal('')))
score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(9.9), StringVal('')))
score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))
score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))

input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
input_table = Store(input_table, StringVal('Name'), name_rows)
input_table = Store(input_table, StringVal('Age'), age_rows)
input_table = Store(input_table, StringVal('Score'), score_rows)

input_col_names = ['Name', 'Age', 'Score']
num_input_rows = 5

if __name__ == "__main__":
#         # OUTPUT TABLE avg score
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)
#     output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Max Score'), output_age_rows)
#     output_col_names = ['Max Score']
#     num_output_rows = 1

#     print('Test avg score')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')

    #      # OUTPUT TABLE sum score
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_score_rows = Array('output_score_rows', IntSort(), Cell)
    output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(100), StringVal('')))
    output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_table = Store(output_table, StringVal('Max Score'), output_score_rows)
    output_col_names = ['Age', 'Max Score']
    num_output_rows = 2

    print('Test having 1')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

    #  # OUTPUT TABLE sum score
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(222.4), StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Sum_score'), output_age_rows)
    # output_col_names = ['Sum_score']
    # num_output_rows = 1

    # print('Test sum score')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    # print('')

    # # OUTPUT TABLE count 1
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 5, RealVal(5), StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Count'), output_age_rows)
    # output_col_names = ['Count']
    # num_output_rows = 1

    # print('Test count 1 - count number of rows')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    # print('')

    # OUTPUT TABLE count 2
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 1, RealVal(1), StringVal('')))
    # output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 1, RealVal(1), StringVal('')))
    # output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 3, RealVal(3), StringVal('')))

    # output_age_rows2 = Array('output_age_row2', IntSort(), Cell)
    # output_age_rows2 = Store(output_age_rows2, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    # output_age_rows2 = Store(output_age_rows2, 1, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    # output_age_rows2 = Store(output_age_rows2, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Age'), output_age_rows2)
    # output_table = Store(output_table, StringVal('Count'), output_age_rows)
    # output_col_names = ['Age', 'Count']
    # num_output_rows = 3

    # print('Test count 2 - group 3 together by name')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    # print('')

    # # OUTPUT TABLE avg score
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(44.48), StringVal('')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('Avg Score'), output_age_rows)
    # output_col_names = ['Avg Score']
    # num_output_rows = 1

    # print('Test avg score')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    # print('')

    # OUTPUT TABLE avg age
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)
#     output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(112) / RealVal(5), StringVal('')))

# #     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
# #     output_table = Store(output_table, StringVal('Age'), output_age_rows)
# #     output_col_names = ['Age']
# #     num_output_rows = 1

#     print('Test avg age')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('AGE'), output_age_rows)
#     output_col_names = ['AGE']
#     num_output_rows = 2

#     print('Test 3 - only 20 and 21')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')


#     # OUTPUT TABLE 4
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)
#     output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 20, RealVal(20), StringVal('')))
#     output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
#     output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
#     output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 24, RealVal(24), StringVal('')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Age'), output_age_rows)
#     output_col_names = ['Age']
#     num_output_rows = 4

#     print('Test 4 - not 25')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')


#     # OUTPUT TABLE 5
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Age'), output_age_rows)
#     output_col_names = ['Age']
#     num_output_rows = 0

#     print('Test 5 - empty output table')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')


#     # OUTPUT TABLE 6
#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_col_names = []
#     num_output_rows = 0

#     print('Test 6 - should be unsat')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')


    # OUTPUT TABLE 7


    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    age_rows = Array('age_rows', IntSort(), Cell)
    age_rows = Store(age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    age_rows = Store(age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    age_rows = Store(age_rows, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    age_rows = Store(age_rows, 3, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    age_rows = Store(age_rows, 4, cell(StringVal('int'), 21, RealVal(21), StringVal('')))

    score_rows = Array('score_rows', IntSort(), Cell)
    score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
    score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(12.5), StringVal('')))
    score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
    score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(9.9), StringVal('')))
    score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))

    input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
    input_table = Store(input_table, StringVal('Name'), name_rows)
    input_table = Store(input_table, StringVal('Age'), age_rows)
    input_table = Store(input_table, StringVal('Score'), score_rows)
   
   
	# output basic select all
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    output_age_rows = Store(output_age_rows, 4, cell(StringVal('int'), 21, RealVal(21), StringVal('')))

    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    output_name_rows = Store(output_name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))



    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    output_col_names = ['NAME', 'AGE']
    num_output_rows = 5

    print('Test 8 - selct name and ages')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

    # OUTPUT TABLE 8
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 21, RealVal(21), StringVal('')))



    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    output_col_names = ['NAME', 'AGE']
    num_output_rows = 4

    print('Test 8 - exclude Udit')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')


#     # OUTPUT TABLE 9
#     output_name_rows = Array('output_name_rows', IntSort(), Cell)
#     output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
#     output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Name'), output_name_rows)
#     output_col_names = ['Name']
#     num_output_rows = 2

#     print('Test 9 - only vids and meds')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')


    # OUTPUT TABLE where 
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    output_score_rows = Array('output_score_rows', IntSort(), Cell)
    output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(50), StringVal('')))
    output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(50), StringVal('')))
    output_score_rows = Store(output_score_rows, 2, cell(StringVal('real'), 0, RealVal(100), StringVal('')))


    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('score'), output_score_rows)
    output_table = Store(output_table, StringVal('Passing students'), output_name_rows)



    output_col_names = ['Passing students', 'score']
    num_output_rows = 3

    print('Test where - score >= 50 - YOU SHALL PASS')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')



    # OUTPUT TABLE 10

    output_count_rows = Array('output_count_rows', IntSort(), Cell)
    output_count_rows = Store(output_count_rows, 0, cell(StringVal('int'), 2, RealVal(2), StringVal('')))
    output_count_rows = Store(output_count_rows, 1, cell(StringVal('int'), 1, RealVal(1), StringVal('')))

    output_score_rows = Array('output_score_rows', IntSort(), Cell)
    output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(50), StringVal('')))
    output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(100), StringVal('')))


    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('score'), output_score_rows)
    output_table = Store(output_table, StringVal('number'), output_count_rows)


    output_col_names = ['number', 'score']
    num_output_rows = 2

    print('Test count - score >= 50 - YOU SHALL PASS')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')
  

