import time
import datetime
from copy import deepcopy


# The naive approach is used as baseline. 
# The idea is to find all possible configuration of the `NxN` chess board with `N` queens 
# and check which configuration satisfies the constraint

# Function to create N x N board
def create_board(number_of_queens):
    board = []
    for i in range(0, number_of_queens):
        board.append(['_'] * number_of_queens)
    return board

# Function to print N x N board
def print_board(board):
    for row in board:
        print(str(row).replace(',', ' ').replace('\'', ''))
    print()

# Function to check if two queens are conflicting each other or not
def is_safe_move(board, row, col):

    # return false if two queens share the same column
    for i in range(len(board)):
        if board[i][col] == 'Q' and i != row:
            return False

    # return false if two queens share the same row
    for i in range(len(board)):
        if board[row][i] == 'Q' and i != col:
            return False

    # return false if two queens share the same enitre primary diagonal
    r = row
    c = col
    while r >= 0 and c < len(board):
        if board[r][c] == 'Q' and row != r and col != c:
            return False
        r -= 1
        c += 1

    r = row
    c = col
    while r < len(board) and c >= 0:
        if board[r][c] == 'Q' and row != r and col != c:
            return False
        r += 1
        c -= 1

    # return false if two queens share the same entire secondary diagonal
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q' and row != r and col != c:
            return False
        r -= 1
        c -= 1

    r = row
    c = col
    while r < len(board) and c < len(board):
        if board[r][c] == 'Q' and row != r and col != c:
            return False
        r += 1
        c += 1

    return True

def no_conflict(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                if not is_safe_move(board, row, col):
                    return False
    return True

def n_queen(board, row):

    # if 'N' queens are placed successfully i.e all rows are explored, print the board
    if row == len(board):
        # b = deepcopy(board)
        # configurations.append(b)
        if no_conflict(board):
            print_board(board)
        return

    # place queen at every column in the current row 'row' and recursively call for each valid movement
    for col in range(len(board)):
        # place queen on the current square in board
        board[row][col] = 'Q'

        # recursively call for the next row
        n_queen(board, row + 1)

        # reset the current square
        board[row][col] = '_'

# def print_solutions(configurations):
#     for board in configurations:
#         if no_conflict(board):
#             print_board(board)

def main(N=None):
    if N:
        number_of_queens = N
    else:
        number_of_queens = int(input('Enter number of queens, N \n'))
    start_time=datetime.datetime.now()
    # configurations = []
    if number_of_queens <= 3:
        print("Solution does not exist")
    else:
        board = create_board(number_of_queens)
        n_queen(board, 0)
        # print_solutions(configurations)
    end_time=datetime.datetime.now()
    Time_diff=end_time-start_time
    Time_diff=Time_diff.total_seconds()*1000
    return Time_diff

if __name__ == '__main__':
    main()