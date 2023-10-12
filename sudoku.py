def findNextEmpty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet
    #return row, col or None, None if there is none

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def isValid(puzzle, guess, row, col):
    #check the row
    rowVals = puzzle[row]
    if guess in rowVals:
        return False
    
    #check the column
    colVals = [puzzle[i][col] for i in range(9)]
    if guess in colVals:
        return False
    
    #check the square
    #we want to know where the 3*3 square starts
    rowStart = (row // 3)*3
    colStart = (col // 3)*3
    for r in range(rowStart, rowStart+3):
        for c in range(colStart, colStart+3):
            if puzzle[r][c] == guess:
                return False
    
    #if we get here, these checks pass
    return True


def solveSudoku(puzzle):
    #step 1 : choose somewhere on the puzzle to make a guess
    row, col = findNextEmpty(puzzle)
    if row == None:
        return True     #if there is no more empty row, it means that the sudoku is solved
    
    #step 2 : if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  #range(1, 10) is 1,2,...,9
        #step 3 : check if this is a valid guess
        if isValid(puzzle, guess, row, col):
            #if it's valid, place this guess in the puzzle
            puzzle[row][col] = guess
            #step 4 : recursively call our function
            if solveSudoku(puzzle):
                return True
        
        #step 5 : if not valid OR if our guess doesn't solve the puzzle, try a new number
        puzzle[row][col] = -1   #reset the guess
    
    #step 6 : if none of the numbers that we try work, then this puzzle is unsolvable
    return False

if __name__=='__main__':
    exampleBoard = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,    -1, 8, -1],
        
        [-1, 5, -1,   -1, 6, 8,    -1, -1, -1],
        [2, -1, 6,    -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],
        
        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,   -1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1],
    ]
    print(solveSudoku(exampleBoard))
    print(exampleBoard)


