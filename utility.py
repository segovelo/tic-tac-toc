import sys
# return -1 if "o" wins, 0 if nobody wins and 1 if "x" wins

def check_row(rows):
    for row in rows:
        if row[0]==row[1] and row[1]==row[2]:
            return row[0]
    return "n"

def check_column(rows):
    for j in range(0,len(rows[0])):
        if rows[0][j]==rows[1][j] and rows[1][j]==rows[2][j]:
            return rows[0][j]
    return "n"

def check_diagonal(rows):
    i = 0
    winner_found=False
    for j in range(0,len(rows[0])-1):
        if rows[j][j]==rows[j+1][j+1]:
            winner_found=True
        else:
            winner_found=False
            break
    if winner_found: return rows[0][0]
    winner_found=False
    for j in range(len(rows[0])-1, 0, -1):
        if rows[len(rows[0])-j-1][j]==rows[len(rows[0])-j][j-1]:
            winner_found=True
        else:
            winner_found=False
            break
    if winner_found: return rows[0][len(rows[0])-1]
    return "n"


states=[[["x","o","o"],["o","x","o"],["x","o","o"]],[["x","o","x"],["x","o","o"],["o","x","o"]],[["x","o","o"],["x","x","x"],["o","x","o"]],[["x","x","o"],["o","o","x"],["o","x","x"]],[["x","o","o"],["o","x","o"],["o","x","x"]]]
winner_found = False
for state in states:
    winner = check_row(state)
    if winner == "n":
        winner = check_column(state)
    if winner == "n":
        winner = check_diagonal(state)
    print ("winner is : ", winner)
