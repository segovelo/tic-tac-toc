import sys
# return -1 if "o" wins, 0 if nobody wins and 1 if "x" wins

def check_row(rows):
    for row in rows:
        if row[0]==row[1] and row[1]==row[2]:
            return row[0]
    return "n"

def check_column(columns):
    for column in columns:
        if column[0]==column[1] and column[1]==column[2]:
            return column[0]
    return "n"

states=[[["x","o","o"],["o","x","o"],["x","o","o"]],[["x","o","x"],["x","o","o"],["o","x","o"]],[["x","o","o"],["o","x","o"],["o","x","x"]]]
winner_found = False
for state in states and not winner_found:
    winner = check_row(state)
    if winner == "n":
        columns = [[]]
        for row in state:
            columns[row.index].append(row)
        winner = check_column(columns)
