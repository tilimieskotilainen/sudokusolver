import copy


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


for jeah in range(9):
    print(sudoku[jeah])

potentials = copy.deepcopy(sudoku)
squares = [[],[],[],
           [],[],[],
           [],[],[]]
columns = copy.deepcopy(squares)
pot_squares = copy.deepcopy(squares)
pot_columns = copy.deepcopy(columns)


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


#Initialize squares and columns
for row_indexus in range(9):
    for col_indexus in range(9):
        sq_num, sq_item = square_item(row_indexus, col_indexus)
        squares[sq_num].append(sudoku[row_indexus][col_indexus])
        columns[col_indexus].append(sudoku[row_indexus][col_indexus])


def update_sudoku(row_num, column_num, number): #Updates the sudoku and the column / square versions of it with new number
    global sudoku
    global squares
    global columns
    global potentials
    global pot_squares
    global pot_columns
    
    #Update specific cell in sudoku with found number
    sudoku[row_num][column_num] = number

    #Update specific cell in columns with found number
    columns[column_num][row_num] = number

    #Update specific cell in squares with found number
    sq_num, sq_index_pos = square_item(row_num, column_num)
    squares[sq_num][sq_index_pos] = number

    #Determine potential numbers based on row, column and square

    cell_potentials = [] #Empty container for temporary saving of the potential numbers in a cell
    for row_num in range(9):
        for col_num in range(9):
            if sudoku[row_num][col_num] == 0:
                sq_num, sq_index = square_item(row_num, col_num)
                #Testing each number between 1 and 9, test whether it is a potential one based on row, column and square of the current cell
                for j in range(1,10):
                    if j not in sudoku[row_num] and j not in columns[col_num] and j not in squares[sq_num]:
                        cell_potentials.append(j) #If number being tested is not found in related cells, add to temporary container

                #Error handling in case no potentials are found
                if len(cell_potentials) == 0:
                    print("Error, no potentials found", row_num, col_num, cell_potentials)
                    exit()

                #Save the list of potential numbers for the cell in the corresponding cell in the matrix of potential numbers
                potentials[row_num][col_num] = cell_potentials
#                print("Cell potentials:", cell_potentials)

            else:
                #If the cell in question has already been populated in the sudoku, copy that number to the corresponding cell in the matrix of potential numbers
                potentials[row_num][col_num] = sudoku[row_num][col_num]

            cell_potentials = [] #Empty out the container for potential numbers

    #Copy the potential numbers found for each cell into the corresponding locations in the square potentials -matrix
    for row_number in range(9):
        for col_number in range(9):
            sq_num, sq_item = square_item(row_number, col_number)
            pot_squares[sq_num].append(potentials[row_number][col_number])

    #Copy the potential numbers found for each cell into the corresponding locations in the column potentials -matrix
    for row_order in range(9):
        for col_order in range(9):
            pot_columns[col_order].append(potentials[row_order][col_order])

#    print("Potentials:", potentials)


def test_potentials(row, col, the_cell):

    global sudoku

    row_all_pots = [] #List to store all the possible numbers in the related cells (in row + column + square)
    col_all_pots = []
    sq_all_pots = []
    #JOS JOKU POTENTIAALINEN EI OLE MISSÄÄN SAMAN RIVIN, SARAKKEEN TAI NELIÖN POTENTIAALISESSA, SE VALITAAN


    for each_cell_of_potentials_row in potentials[row]:
        if type(each_cell_of_potentials_row) == list:
            row_all_pots = row_all_pots + each_cell_of_potentials_row

    for each_cell_of_potentials_col in pot_columns[col]:
        if type(each_cell_of_potentials_col) == list:
            col_all_pots = col_all_pots + each_cell_of_potentials_col

    square, square_cell = square_item(row, col)
    for each_cell_of_potentials_sq in pot_squares[square]:
        if type(each_cell_of_potentials_sq) == list:
            sq_all_pots = sq_all_pots + each_cell_of_potentials_sq

    for one_potential_of_cell in the_cell:
        row_occurences = row_all_pots.count(one_potential_of_cell)
        col_occurences = col_all_pots.count(one_potential_of_cell)
        sq_occurences = sq_all_pots.count(one_potential_of_cell)

        if row_occurences == 1 or col_occurences == 1 or sq_occurences == 1:
            update_sudoku(row, col, one_potential_of_cell)
            for jau in range(9):
                print("updated sudoku:", sudoku[jau])
            break
    row_all_pots = []
    col_all_pots = []
    sq_all_pots = []
    

def test_cycle():
    global sudoku
    global potentials

    #create potentials by running the update sudoku function. Artificially pass the value of the first cell.
    first_cell = sudoku[0][0]
    update_sudoku(0, 0, first_cell)

    #Start running through the sudoku 100 times
    for iteration in range(6):
        print("Iteration", iteration)
        for row in range(9):
            for col in range(9):
                the_cell = potentials[row][col]
                if type(the_cell) == list:
                    if len(the_cell) > 1: #Only look at options if there are many options in a list
                        test_potentials(row, col, the_cell)
                    elif len(the_cell) == 1:
                        update_sudoku(row, col, the_cell[0])

    for juu in range(9):
        print(sudoku[juu])

    for jaa in range(9):
        print(potentials[jaa])


test_cycle()