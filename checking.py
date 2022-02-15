
def check(arrive):
    if arrive[0][0] == arrive[1][1] == arrive[2][2]: return arrive[2][2]
    if arrive[0][2] == arrive[1][1] == arrive[2][0]: return arrive[2][0]

    for l in range(3):
        if arrive[l][0] == arrive[l][1] == arrive[l][2]: return arrive[l][2]

    for c in range(3):
        if arrive[0][c] == arrive[1][c] == arrive[2][c]: return arrive[2][c]