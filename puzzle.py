import sys
import time
import numpy as np

puzzle_icon = '''
69696969696969696969696969696996969696969696969696969696969696969696969696969696969696969696969696
69696969696969696969696969696996969696969696969696969696969696969696969696969696969696969696969696
696              696     696969     696            696          6969     6969696969            666
969     6969     969     696969     969696969     96969696     96969     6969696969     6969696969
696     6969     696     696969     96969696     96969696     969696     6969696969     6969696969
969              969     696969     9696969     96969696     9696969     6969696969          69696
696     969696969696     696969     969696     96969696     96969696     6969696969          69696
969     969696969696     696969     96969     96969696     969696969     6969696969     6969696969
696     969696969696     696969     6969     69696969     6969696969     6969696969     6969696969
969     969696969696                969          969            9696            969            969
69696969696969696969696969696996969696969696969696969696969696969696969696969696969696969696969696
6969696969696969696969696969699696969696969696969696969696969696969696969696969696969696966@charan
'''
# printing above icon
print(puzzle_icon)


# this function checks soduku possibilities
def check_possible(x, y, n):
    # This checks check if given number is already present in the row
    # if present return false
    for i in range(0, 9):
        if input_puzzle[x][i] is n:
            return False
            
    # This checks check if given number is already present in the column
    # if present return false
    for j in range(0, 9):
        if input_puzzle[j][y] is n:
            return False

    # this function selects the square for particular x and y value. e.g.
    # for x = 0, y = 0 then it will be in the first box
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    # this will check if the given number is already present in the square box
    # if present return false else return true and put that value for that cell
    for i in range(0, 3):
        for j in range(0, 3):
            if input_puzzle[x1 + i][y1 + j] is n:
                return False
    return True


# This function solves the puzzle
def puzzle_solver():
    try:
        for x in range(9): 
            for y in range(9):
                # if zero is present in the particular cell then continue else 
                # search for next cell with zero value
                if input_puzzle[x][y] is 0:
                    # this will check all the possible value from 1 to 9
                    for n in range(1, 10):
                        # call check_possible function for every values from 1 to 9.
                        # if it returns true then we will put that value into the cell
                        if check_possible(x, y, n):
                            input_puzzle[x][y] = n
                            # again call puzzle solver for next cell
                            puzzle_solver()
                            # sometimes times we cant fill any values from 1 to 9
                            # then put the initial value and go back to the previous
                            # cell and change to the next number. ie suppose 4 is present
                            # in the previous cell then change it to next number 5. like that
                            # using recursion we can fill the cells
                            input_puzzle[x][y] = 0
                    return

        print('===========================================================\n')
        # this will print the 2d matrix in readble matrix form
        print(np.matrix(input_puzzle))
        input('\nPlease enter to find other possible solutions ')
        print('\nSolving...\n')
    except BaseException as e:
        print('\n', e)


input_format = '''
800000000
003600000
070090200
050007000
000045700
000100030
001000068
008500010
090000400
'''

print('::Example::')
print(input_format)

# size of list
size = 9
# list to store the puzzle data
input_puzzle = []


def enter_data():
    for x_ in range(size):
        try:
            # using list we can able to split string of data into list format
            input_number = list(input())
            # using list comprehension we are creating 2d matrx, and converting string
            # to integer int(y_)
            input_puzzle.append([int(y_) for y_ in input_number])
        except BaseException as e:
            print('\n', e)


KEEP_RUNNING_OUTER_LOOP = True
# using while loop we are execu
while KEEP_RUNNING_OUTER_LOOP:
    print('\n===========================================================\n')
    print("Enter the numbers in above format. For empty cells fill 0")
    
    # calling enter_data for getting input
    enter_data()
    print('\nSolving...\n')
    puzzle_solver()

    KEEP_RUNNING_INNER_LOOP = True
    # while while loop is used to make next decision
    while KEEP_RUNNING_INNER_LOOP:
        try:
            decision = input('\nWould you like to solve another puzzle? (YyNn): ')

            if decision is '':
                print('You pressed ENTER key')
            elif decision in 'Yy':
                input_puzzle.clear()
                KEEP_RUNNING_INNER_LOOP = False
            elif decision in 'Nn':
                KEEP_RUNNING_INNER_LOOP = False
                KEEP_RUNNING_OUTER_LOOP = False
                print('Exiting...')
            else:
                print('Enter the valid input')

        except BaseException as e:
            print('\n', e)


CLOSING_TIME = 5

# This while loop is just used to display closing time after we give N or n for
# the terminal. It will count from 5 to 1
while True:
    sys.stdout.write('\rClosing in {} sec'.format(CLOSING_TIME))
    sys.stdout.flush()
    time.sleep(1)
        
    CLOSING_TIME -= 1
    if CLOSING_TIME == 0:
        break
