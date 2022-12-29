sudoku = [
[0, 0, 2, 0, 3, 0, 4, 0, 6],
[0, 0, 6, 2, 0, 0, 9, 3, 0],
[9, 3, 0, 0, 0, 0, 0, 0, 2],
[0, 5, 7, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 8, 6, 0, 0, 4],
[4, 0, 0, 0, 1, 0, 7, 0, 0],
[0, 0, 1, 3, 9, 5, 0, 0, 0],
[3, 7, 0, 4, 0, 0, 0, 1, 0],
[8, 0, 0, 0, 0, 1, 0, 0, 3]
]

"""potentials = [[],[],[],
           [],[],[],
           [],[],[]]"""

#Range(1:10)

squares = [[],[],[],
           [],[],[],
           [],[],[]]
columns = [[],[],[],
           [],[],[],
           [],[],[]]

range1 = [0, 1, 2]
range2 = [3, 4, 5]
range3 = [6, 7, 8]

#sudoku to columns conversion: row/column translates to column/row
#sudoku to squares conversion: jos rangen eka rivi, 0 + sarakerangen

def square_item(row, column):
    if row in range1:
        if column in range1:
            sq_item = (row * 3) + column
            square_num = 0
        if column in range2:
            sq_item = (row * 3) + column - 3
            square_num = 1
        if column in range3:
            sq_item = (row * 3) + column - 6
            square_num = 2
    if row in range2:
        if column in range1:
            sq_item = ((row - 3) * 3) + column
            square_num = 3
        if column in range2:
            sq_item = ((row - 3) * 3) + column - 3
            square_num = 4
        if column in range3:
            sq_item = ((row - 3) * 3) + column - 6
            square_num = 5
    if row in range3:
        if column in range1:
            sq_item = ((row - 6) * 3) + column
            square_num = 6
        if column in range2:
            sq_item = ((row - 6) * 3) + column - 3
            square_num = 7
        if column in range3:
            sq_item = ((row - 6) * 3) + column - 6
            square_num = 8
    
    return square_num, sq_item
#    print("Square:", square_num, " index position:", sq_item)


#Initialize squares
for row_index in range(9):
    for col_index in range(9):
        sq_num, sq_item = square_item(row_index, col_index)
        squares[sq_num].append(sudoku[row_index][col_index])

#Initialize columns
for row_index in range(9):
    for col_index in range(9):
        columns[col_index].append(sudoku[row_index][col_index])

def update_sudoku(row_num, column_num, number):
    sudoku[row_num][column_num] = number
    sq_num, sq_index_pos = square_item(row_num, column_num)
    squares[sq_num][sq_index_pos] = number
    columns[column_num][row_num] = number
    
    print("Sudoku:", sudoku)
    print("Squares:", squares)
    print("Columns:", columns)

#############################################################
    #END OF BASIC INITIALIZATIONS AND CONVERSION FUNCTIONS


#Determine potential numbers based on row, column and square
def determine_potentials()
    potentials = sudoku
    cell_potentials = []
    for row_index in range(9):
        for col_index in range(9):
            if sudoku[row_index][col_index] == 0:
                sq_num, sq_index = square_item(row_index, col_index)
                for j in range(1,10):
                    if j not in sudoku[row_index] and j not in columns[col_index] and j not in squares[sq_num]:
                        cell_potentials.append(j)
                potentials[row_index][col_index] = cell_potentials
            cell_potentials = []

########################################
#END OF DETERMINING POTENTIALS FOR EACH CELL
            
#compare potentials of each cell against potentials in row, column and square to determine unique potentials

def compare_potentials():
    
