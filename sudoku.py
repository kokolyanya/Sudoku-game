import random, re

def findNextEmpty(puzzle) :
    #finds the next row, col on the puzzle that's not filled yet
    #return row, col or None, None if there is none

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def isValid(puzzle, guess, row, col) :
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


def solveSudoku(puzzle) :
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

def newPuzzle() :
    puzzle = [[-1 for _ in range(9)] for _ in range(9)]
    compteur = 0
    row = 0    #the row
    col = 0    #the column
    while compteur < 9:
        guess = random.randint(1, 9)    #the number
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            col += 1
            compteur += 1

    return puzzle

def userPuzzle(puzzle) :
    userPuzzle = [[0 for _ in range(9)] for _ in range(9)]
    compteur = 0
    while compteur < 70:
        row = random.randint(0, 8)    #the row
        col = random.randint(0, 8)    #the col
        if userPuzzle[row][col] == 0 :
            userPuzzle[row][col] = puzzle[row][col]
            compteur += 1

    return userPuzzle

def play(puzzle, userPuzzle) :
    lives = 3
    while lives > 0 and puzzle != userPuzzle:
        printPuzzle(userPuzzle)
        userInput = re.split(',(\\s)*',input("Choose a square to fill. Input as row,col : "))
        try:
            row, col = int(userInput[0])-1, int(userInput[-1])-1
        except ValueError:
            continue
        if row<0 or row>=9 or col<0 or col>=9 : #if the row or column is invalid
            print("Invalid location. Try again !")
            continue
        guess = input("Enter the number : ")
        try:
            number = int(guess)
        except ValueError:
            print("Invalid input. Enter a number !")
            continue
        if userPuzzle[row][col] == 0 :
            if puzzle[row][col] == number :
                userPuzzle[row][col] = number
            else :
                lives -= 1
                print(f'Wrong number ! You have {lives} lives left.')
        else :
            print("Sorry, try again !")
            continue
    if lives == 0 :
        print(":(:(:(:(:(:(:(:(:(:(")
        print(":(:( GAME OVER  :(:(")
        print(":(:(:(:(:(:(:(:(:(:(")
        printPuzzle(puzzle)
    else :
        print("**********************************")
        print("** CONGRATULATIONS, YOU WIN !!! **")
        print("**********************************")

def printPuzzle(puzzle) :
    for r in range(9) :
        row = [puzzle[r][c] for c in range(0,3)]
        row1 = [puzzle[r][c] for c in range(3,6)]
        row2 = [puzzle[r][c] for c in range(6,9)]
        print(row, row1, row2)
        if r % 3 == 2:
            print('')


if __name__=='__main__' :
    print("***** Welcome, this is a sudoku game ! Let's play, goooooo *****\n")
    puzzle = newPuzzle()
    solveSudoku(puzzle)
    userPuzzle = userPuzzle(puzzle)
    play(puzzle, userPuzzle)

