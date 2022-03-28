# Function to create N x N board
def create_board(num_queens):
    board = []
    for i in range(0, num_queens):
        board.append(['_'] * num_queens)
    return board

# Function to print N x N board
def print_board(board):
    for row in board:
        print(str(row).replace(',', ' ').replace('\'', ''))
    print()

# Function to check if two queens threaten each other or not
def is_safe_move(board, row, col):

    # return false if two queens share the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # return false if two queens share the same primary diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # return false if two queens share the same secondary diagonal
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True

def n_queen(board, row):

    # if `N` queens are placed successfully, print the board
    if row == len(board):
        print_board(board)
        return

    # place queen at every column in the current row `row` and recursively call for each valid movement
    for col in range(len(board)):

        # if no two queens threaten each other
        if is_safe_move(board, row, col):
            # place queen on the current square
            board[row][col] = 'Q'

            # recursively call for the next row
            n_queen(board, row + 1)

            # reset the current square
            board[row][col] = '_'


if __name__ == '__main__':

    # `N × N` chessboard
    num_queens = int(input('Enter number of queens, N \n'))
    board = create_board(num_queens)
    n_queen(board, 0)
