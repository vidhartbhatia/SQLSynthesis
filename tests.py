from z3 import *
from synthesis import solve, Cell, cell

# To run our tests, run python3 tests.py

# INPUT TABLE
name_rows = Array('name_rows', IntSort(), Cell)
name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))
name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))

age_rows = Array('age_rows', IntSort(), Cell)
age_rows = Store(age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
age_rows = Store(age_rows, 1, cell(StringVal('int'), 20, RealVal(20), StringVal('')))
age_rows = Store(age_rows, 2, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
age_rows = Store(age_rows, 3, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
age_rows = Store(age_rows, 4, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

score_rows = Array('score_rows', IntSort(), Cell)
score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(75.0), StringVal('')))
score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(9.9), StringVal('')))
score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))
score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(12.5), StringVal('')))

input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
input_table = Store(input_table, StringVal('Name'), name_rows)
input_table = Store(input_table, StringVal('Age'), age_rows)
input_table = Store(input_table, StringVal('Score'), score_rows)

input_col_names = ['Name', 'Age', 'Score']
num_input_rows = 5

if __name__ == "__main__":
    # OUTPUT TABLE SELECT
    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))
    name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))

    age_rows = Array('age_rows', IntSort(), Cell)
    age_rows = Store(age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    age_rows = Store(age_rows, 1, cell(StringVal('int'), 20, RealVal(20), StringVal('')))
    age_rows = Store(age_rows, 2, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    age_rows = Store(age_rows, 3, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    age_rows = Store(age_rows, 4, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_table = Array('output', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('NAME'), name_rows)
    output_table = Store(output_table, StringVal('AGE'), age_rows)
    output_col_names = ['NAME', 'AGE']
    num_output_rows = 5

    print('Test SELECT')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test SELECT
# Query generated:
# "SELECT Name AS NAME, Age AS AGE FROM input_table"
# without group by, in time 0.24 


    # OUTPUT TABLE WHERE
    name_rows = Array('name_rows', IntSort(), Cell)
    name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    score_rows = Array('score_rows', IntSort(), Cell)
    score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(75.0), StringVal('')))
    score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
    score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Passing students'), name_rows)
    output_table = Store(output_table, StringVal('Score'), score_rows)
    output_col_names = ['Passing students', 'Score']
    num_output_rows = 3

    print('Test WHERE')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test WHERE
# Query generated:
# "SELECT Name AS Passing students, Score AS Score FROM input_table WHERE Score >= 50"
# without group by, in time 0.31 


    # OUTPUT TABLE AVG
    output_score_rows = Array('output_score_rows', IntSort(), Cell)
    output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(49.48), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Avg Score'), output_score_rows)
    output_col_names = ['Avg Score']
    num_output_rows = 1

    print('Test AVG')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test AVG
# Query generated:
# "SELECT AVG(Score) AS Avg Score FROM input_table"
# with group by, in time 36.78


    # OUTPUT TABLE COUNT
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 20, RealVal(20), StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_count_rows = Array('output_count_rows', IntSort(), Cell)
    output_count_rows = Store(output_count_rows, 0, cell(StringVal('int'), 1, RealVal(1), StringVal('')))
    output_count_rows = Store(output_count_rows, 1, cell(StringVal('int'), 1, RealVal(1), StringVal('')))
    output_count_rows = Store(output_count_rows, 2, cell(StringVal('int'), 2, RealVal(2), StringVal('')))
    output_count_rows = Store(output_count_rows, 3, cell(StringVal('int'), 1, RealVal(1), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_table = Store(output_table, StringVal('Count'), output_count_rows)
    output_col_names = ['Age', 'Count']
    num_output_rows = 4

    print('Test COUNT')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test COUNT
# Query generated:
# "SELECT MIN(Age) AS Age, COUNT(Age) AS Count FROM input_table GROUP BY Age"
# with group by, in time 46.70


# commented out slower tests

#     # OUTPUT TABLE HAVING 
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)
#     output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
#     output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(21), StringVal('')))

#     output_score_rows = Array('output_score_rows', IntSort(), Cell)
#     output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(75.0), StringVal('')))
#     output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(109.9), StringVal('')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Age'), output_age_rows)
#     output_table = Store(output_table, StringVal('Sum of Scores'), output_score_rows)
#     output_col_names = ['Age', 'Sum of Scores']
#     num_output_rows = 2

#     print('Test HAVING')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')

# # Test HAVING
# # Query generated:
# # "SELECT Age AS Age, SUM(Score) AS Sum of Scores FROM input_table WHERE Name >= "Ebru" GROUP BY Age HAVING SUM(Score) >= 75"
# # with having, in time 128.34


#     # OUTPUT TABLE HAVING 2 (I think this was tested with a different input table)
#     output_age_rows = Array('output_age_rows', IntSort(), Cell)
#     output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
#     output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

#     output_score_rows = Array('output_score_rows', IntSort(), Cell)
#     output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(100), StringVal('')))
#     output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Age'), output_age_rows)
#     output_table = Store(output_table, StringVal('Max Score'), output_score_rows)
#     output_col_names = ['Age', 'Max Score']
#     num_output_rows = 2

#     print('Test HAVING 2')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')

# # Test HAVING 2
# # Query generated:
# # "SELECT Age AS Age, MAX(Score) AS Max Score FROM input_table GROUP BY Age HAVING MAX(Score) != 99/10"
# # with having in time 83.11 


     # OUTPUT TABLE max age
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Max age'), output_age_rows)
    output_col_names = ['Max age']
    num_output_rows = 1

    print('Test max age')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test max age
# Query generated:
# "SELECT Age AS Max age FROM input_table WHERE Score = 25/2"
# without group by, in time 0.16 


     # OUTPUT TABLE sum score
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(247.4), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Sum of Scores'), output_age_rows)
    output_col_names = ['Sum of Scores']
    num_output_rows = 1

    print('Test sum score')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test sum score
# Query generated:
# "SELECT SUM(Score) AS Sum of Scores FROM input_table"
# with group by, in time 30.97


    # OUTPUT TABLE count 2
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 5, RealVal(5), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Count'), output_age_rows)
    output_col_names = ['Count']
    num_output_rows = 1

    print('Test COUNT - count number of rows')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test COUNT - count number of rows
# Query generated:
# "SELECT COUNT(Score) AS Count FROM input_table"
# with group by, in time 6.92


    # OUTPUT TABLE avg age
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('real'), 0, RealVal(103) / RealVal(5), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Average Age'), output_age_rows)
    output_col_names = ['Average Age']
    num_output_rows = 1

    print('Test avg age')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test avg age
# Query generated:
# "SELECT AVG(Age) AS Average Age FROM input_table"
# with group by, in time 38.97


    # OUTPUT TABLE where 2
    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 4

    print('Test WHERE - not 20')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test WHERE - not 20
# Query generated:
# "SELECT Age AS Age FROM input_table WHERE Age != 20"
# without group by, in time 2.14 


    # OUTPUT TABLE empty
    output_age_rows = Array('output_age_rows', IntSort(), Cell)

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('Age'), output_age_rows)
    output_col_names = ['Age']
    num_output_rows = 0

    print('Test - empty output table')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test - empty output table
# Unsat 


    # OUTPUT TABLE empty 2
    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_col_names = []
    num_output_rows = 0

    print('Test - should be unsat')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test - should be unsat
# Unsat 


# commented out repeat test

    # # NEW INPUT TABLE 
    # name_rows = Array('name_rows', IntSort(), Cell)
    # name_rows = Store(name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    # name_rows = Store(name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    # name_rows = Store(name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    # name_rows = Store(name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    # name_rows = Store(name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    # age_rows = Array('age_rows', IntSort(), Cell)
    # age_rows = Store(age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # age_rows = Store(age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # age_rows = Store(age_rows, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # age_rows = Store(age_rows, 3, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    # age_rows = Store(age_rows, 4, cell(StringVal('int'), 21, RealVal(21), StringVal('')))

    # score_rows = Array('score_rows', IntSort(), Cell)
    # score_rows = Store(score_rows, 0, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
    # score_rows = Store(score_rows, 1, cell(StringVal('real'), 0, RealVal(12.5), StringVal('')))
    # score_rows = Store(score_rows, 2, cell(StringVal('real'), 0, RealVal(50.0), StringVal('')))
    # score_rows = Store(score_rows, 3, cell(StringVal('real'), 0, RealVal(9.9), StringVal('')))
    # score_rows = Store(score_rows, 4, cell(StringVal('real'), 0, RealVal(100.0), StringVal('')))

    # input_table = Array('input_table', StringSort(), ArraySort(IntSort(), Cell))
    # input_table = Store(input_table, StringVal('Name'), name_rows)
    # input_table = Store(input_table, StringVal('Age'), age_rows)
    # input_table = Store(input_table, StringVal('Score'), score_rows)
   
   
	# # output basic select all
    # output_age_rows = Array('output_age_rows', IntSort(), Cell)
    # output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 22, RealVal(22), StringVal('')))
    # output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    # output_age_rows = Store(output_age_rows, 4, cell(StringVal('int'), 21, RealVal(21), StringVal('')))

    # output_name_rows = Array('output_name_rows', IntSort(), Cell)
    # output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
    # output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    # output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Udit')))
    # output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    # output_name_rows = Store(output_name_rows, 4, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))

    # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    # output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    # output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    # output_col_names = ['NAME', 'AGE']
    # num_output_rows = 5

    # print('Test 8 - selct name and ages')
    # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    # print('')


    # OUTPUT TABLE exclude udit
    output_name_rows = Array('output_name_rows', IntSort(), Cell)
    output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))
    output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Ebru')))
    output_name_rows = Store(output_name_rows, 2, cell(StringVal('string'), 0, RealVal(0), StringVal('Jeremy')))
    output_name_rows = Store(output_name_rows, 3, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))

    output_age_rows = Array('output_age_rows', IntSort(), Cell)
    output_age_rows = Store(output_age_rows, 0, cell(StringVal('int'), 19, RealVal(19), StringVal('')))
    output_age_rows = Store(output_age_rows, 1, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 2, cell(StringVal('int'), 21, RealVal(21), StringVal('')))
    output_age_rows = Store(output_age_rows, 3, cell(StringVal('int'), 22, RealVal(22), StringVal('')))

    output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
    output_table = Store(output_table, StringVal('AGE'), output_age_rows)
    output_table = Store(output_table, StringVal('NAME'), output_name_rows)
    output_col_names = ['NAME', 'AGE']
    num_output_rows = 4

    print('Test - exclude Udit')
    solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
    print('')

# Test - exclude Udit
# Query generated:
# "SELECT Name AS NAME, Age AS AGE FROM input_table WHERE Age != 20"
# without group by, in time 0.29


# commenting out slower tests

#     # OUTPUT TABLE vids meds
#     output_name_rows = Array('output_name_rows', IntSort(), Cell)
#     output_name_rows = Store(output_name_rows, 0, cell(StringVal('string'), 0, RealVal(0), StringVal('Medha')))
#     output_name_rows = Store(output_name_rows, 1, cell(StringVal('string'), 0, RealVal(0), StringVal('Vidhart')))

#     output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     output_table = Store(output_table, StringVal('Name'), output_name_rows)
#     output_col_names = ['Name']
#     num_output_rows = 2

#     print('Test - only vids and meds')
#     solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     print('')

# # Test - only vids and meds
# # Unsat 


#     # # OUTPUT TABLE count 3
#     # output_count_rows = Array('output_count_rows', IntSort(), Cell)
#     # output_count_rows = Store(output_count_rows, 0, cell(StringVal('int'), 2, RealVal(2), StringVal('')))
#     # output_count_rows = Store(output_count_rows, 1, cell(StringVal('int'), 1, RealVal(1), StringVal('')))

#     # output_score_rows = Array('output_score_rows', IntSort(), Cell)
#     # output_score_rows = Store(output_score_rows, 0, cell(StringVal('real'), 0, RealVal(50), StringVal('')))
#     # output_score_rows = Store(output_score_rows, 1, cell(StringVal('real'), 0, RealVal(100), StringVal('')))

#     # output_table = Array('output_table', StringSort(), ArraySort(IntSort(), Cell))
#     # output_table = Store(output_table, StringVal('score'), output_score_rows)
#     # output_table = Store(output_table, StringVal('number'), output_count_rows)
#     # output_col_names = ['number', 'score']
#     # num_output_rows = 2

#     # print('Test count 3')
#     # solve(input_table, input_col_names, num_input_rows, output_table, output_col_names, num_output_rows)
#     # print('')

