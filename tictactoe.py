"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state(board_size):
    """
    Returns starting state of the board.
    """
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(EMPTY)
        board.append(row)

    """        
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    """
    return board

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)
    if count_x > count_o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]  is not EMPTY:
        raise RuntimeError("The action passed is not valid!")
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def check_rows(board):    
    for row in board:
        winner_found=True
        for i in range(len(row) - 1):
            if row[i]!=row[i+1] or row[i] is EMPTY or row[i+1] is EMPTY:
                winner_found=False
                break
        if winner_found: return row[0]
    return None

def check_columns(board):
    columns = len(board[0])
    for j in range(columns):
        winner_found=True
        for i in range(columns-1):
            if board[i][j]!=board[i+1][j] or board[i][j] is EMPTY or board[i+1][j] is EMPTY:
                winner_found=False
                break
        if winner_found: return board[0][j]
    return None

def check_diagonals(board):
    i = 0
    winner_found=True
    row = len(board[0])
    for j in range(row-1):
        if board[j][j]!=board[j+1][j+1] or board[j][j] is EMPTY or board[j+1][j+1] is EMPTY:
            winner_found=False
            break
    if winner_found: return board[0][0]
    winner_found=True
    for j in range(row-1, 0, -1):
        if board[row-j-1][j]!=board[row-j][j-1] or board[row-j-1][j] is EMPTY or board[row-j][j-1] is EMPTY:
            winner_found=False
            break
    if winner_found: return board[0][row-1]
    return None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = check_rows(board)
    if winner is None:
        winner = check_columns(board)
    if winner is None:
        winner = check_diagonals(board)
    return winner    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X,O] or not actions(board):
        return True
    return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else: 
        return 0

def max_value(board, i):
    if terminal(board) or i > 3:
        return utility(board)
    value = -1000
    for action in actions(board):
        value = max(value,min_value(result(board, action),i+1))
        if value == 1:
            return value
    return value

def min_value(board, i):
    if terminal(board) or i > 3:
        return utility(board)
    value = 1000
    for action in actions(board):
        value = min(value,max_value(result(board, action),i+1))
        if value == -1:
            return value
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    i = 0
    move = ()
    if terminal(board):
        return None
    if player(board) is X:
        value = -1000
        for action in actions(board):
            max = min_value(result(board, action), i)
            if max == 1:
                return action
            if value < max:
                value = max
                move = action
    else:
        value = 1000
        for action in actions(board):
            min = max_value(result(board, action), i)
            if min == -1:
                return  action
            if value > min:
                value = min
                move = action
    return move
    
