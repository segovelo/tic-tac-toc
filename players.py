import sys

def get_player(state):
    count_x = 0
    count_o = 0
    for row in state:
        count_x = count_x + row.count("x")
        count_o = count_o + row.count("o")
    if count_x > count_o:
        return "o"
    return "x"

states=[[["x","",""],["","x",""],["","","o"]],[["","",""],["","",""],["","",""]],[["x","o","o"],["","x",""],["o","x",""]],[["x","x","o"],["","o","x"],["o","x",""]],[["x","",""],["o","x","o"],["o","",""]],[["x","",""],["","x",""],["o","",""]]]
for state in states:
    print("Next player: ", get_player(state))