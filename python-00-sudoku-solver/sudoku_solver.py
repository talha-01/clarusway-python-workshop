puzzle = [
    [0, 0, 0, 1, 0, 5, 0, 6, 8],
    [0, 0, 0, 0, 0, 0, 7, 0, 1],
    [9, 0, 1, 0, 0, 0, 0, 3, 0],
    [0, 0, 7, 0, 2, 6, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 8, 7, 0, 4, 0, 0],
    [0, 3, 0, 0, 0, 0, 8, 0, 5],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [7, 9, 0, 4, 0, 1, 0, 0, 0]
]

# This code solves all sudokus that does NOT require guessing.
green = True
while green:
    green = False
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # possible numbers     
# to list possible number for each 0 in the each rows into the dictioanary row_possible.    
    row_possible = {} 
    for x in range(9):  
        for y in range(9):
            sack = []
            if puzzle[x][y] == 0:
                for i in nums:
                    if i not in puzzle[x]:
                        sack.append(i)
                        key = 'p{}{}'.format(x, y)
                        row_possible[key] = sack
    transpose_puzzle = []  # transpose the puzzle to go through the columns
    row = []        # in the original puzzle. 
    for x in range(9):  
        row = [puzzle[i][x] for i in range(9)]
        transpose_puzzle.append(row)
# to list possible number for each 0 in the each columns into the dictionary column_possible.
    column_possible = {}
    for x in range(9):
        for y in range(9):
            sack = []
            if transpose_puzzle[x][y] == 0:
                for i in nums:
                    if i not in transpose_puzzle[x]:
                        sack.append(i)
                        key = 'p{}{}'.format(y, x)
                        column_possible[key] = sack

    # to turn grids into rows to be able to work on them and label cells with the same key 
    # to compare them with row_possible and column_possible dictionaries.
    grid = []
    grid_index = []  
    for x in [[0,1,2], [3,4,5], [6,7,8]]:
        for y in [[0,1,2],[3,4,5], [6,7,8]]:
            row_1 = []
            row_2 = []
            for z in x:
                for t in y:
                    row_1.append(puzzle[z][t])
                    row_2.append([z, t])
            grid.append(row_1)
            grid_index.append(row_2)
# to list possible numbers for each 0 in the each grid into the dictionary grid_possible.
    grid_possible = {} 
    for x in range(9):
        for y in range(9):
            sack = []
            if grid[x][y] == 0:
                for i in nums:
                    if i not in grid[x]:
                        sack.append(i)
                        key = 'p{}{}'.format(grid_index[x][y][0],grid_index[x][y][1])
                        grid_possible[key] = sack        
# the code below compares row possible values, column possible values, and grid possible values 
# and drops unqualified values for each 0 in the original puzzle.
    unique = {}
    for key in column_possible.keys():  
        all_vals = column_possible[key] + row_possible[key] + grid_possible[key] 
        unique_vals = []
        for i in all_vals:
            if all_vals.count(i) == 3 and i not in unique_vals:
                unique_vals.append(i)
        if len(unique_vals) == 1:
            puzzle[int(key[1])][int(key[2])] = unique_vals[0]
            green = True
        unique[key] = unique_vals
    if unique == {}:  # when all possible values are distributed this code breaks the loop.
        break
if str(puzzle).count('0') == 0:
    for row in puzzle:
        print(row)
else: print('Puzzle requires guessing!')   