import sys
# return -1 if "o" wins, 0 if nobody wins and 1 if "x" wins

X = "x"
O = "o"
EMPTY = ""

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

boards=[[["x","o","o"],["o","x","o"],["x","o","o"]],[["x","o","x"],["x","o","o"],["o","x","o"]],[["x","o","o"],["x","x","x"],["o","x","o"]],[["x","x","o"],["o","o","x"],["o","x","x"]],[["x","o","o"],["o","x","o"],["o","x","x"]],[["x","",""],["","x",""],["o","",""]]]
for board in boards:
    print("board : ", board)
    print ("winner is : ", winner(board))
