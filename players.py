import sys
import copy

X = "x"
O = "o"
EMPTY = ""

def player(state):
    count_x = 0
    count_o = 0
    for row in state:
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
    if board[action[0]][action[1]] is not EMPTY:
        raise RuntimeError("The action passed is not valid!")
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def check_rows(board):
    for row in board:
        if row[0]==row[1] and row[1]==row[2] and row[0] in [X,O]:
            return row[0]
    return None

def check_columns(board):
    for j in range(len(board[0])):
        if board[0][j]==board[1][j] and board[1][j]==board[2][j] and board[0][j] in [X,O]:
            return board[0][j]
    return None

def check_diagonals(board):
    i = 0
    winner_found=False
    for j in range(len(board[0])-1):
        if board[j][j]==board[j+1][j+1] and board[j][j] in [X,O]:
            winner_found=True
        else:
            winner_found=False
            break
    if winner_found: return board[0][0]
    winner_found=False
    for j in range(len(board[0])-1, 0, -1):
        if board[len(board[0])-j-1][j]==board[len(board[0])-j][j-1] and board[len(board[0])-j-1][j] in [X,O]:
            winner_found=True
        else:
            winner_found=False
            break
    if winner_found: return board[0][len(board[0])-1]
    return None

def winner(board):
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
    else: return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    value = -1000
    for action in actions(board):
        value = max(value,min_value(result(board, action)))
        if value == 1:
            return value
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = 1000
    for action in actions(board):
        value = min(value,max_value(result(board, action)))
        if value == -1:
            return value
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = ()
    if terminal(board):
        return None
    if player(board) is X:
        value = -1000
        for action in actions(board):
            max = min_value(result(board, action))
            if value < max:
                value = max
                move = action
    else:
        value = 1000
        for action in actions(board):
            min = max_value(result(board, action))
            if value > min:
                value = min
                move = action

    return move

states=[[["x","",""],["","x",""],["","","o"]],[["","",""],["","",""],["","",""]],[["x","o","o"],["","x",""],["o","x",""]],[["x","x","o"],["","o","x"],["o","x",""]],[["x","",""],["o","x","o"],["o","",""]],[["x","",""],["","x",""],["o","",""]],[["x","o","o"],["x","x","x"],["o","x","o"]],[["x","o","x"],["x","o","x"],["o","x","o"]]]
for state in states:
    print("Next player: ", player(state))
for state in states:
    print("board : ",state)
    print("actions : ", actions(state))
    print("winner : ",winner(state))
    term = terminal(state)
    print("terminal : ", term)
    if(term):
        print("utility : ",utility(state))
"""
for state in states:
    print("board : ",state)
    print("result : ", result(state,(0,2)))
"""
