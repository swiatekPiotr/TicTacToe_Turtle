import turtle
import random
import time

window = turtle.Screen()

size = 600
X = -300
Y = 300

window.setup(size, size)
window.title("Tic Tac Toe")
window.bgcolor('black')

xo = turtle.Turtle()
xo.color('white')
xo.pensize(8)
xo.speed(0)
xo.hideturtle()

arrive = [[None, None, None],
          [None, None, None],
          [None, None, None]]

turn = random.choice(['x', 'o'])

SPACE = size / 3
for a in [1, 2]:
    xo.penup()
    xo.goto(X + a*SPACE, Y)
    xo.pendown()
    xo.goto(X + a*SPACE, -Y)

    xo.penup()
    xo.goto(X, Y - a * SPACE)
    xo.pendown()
    xo.goto(-X, Y - a * SPACE)

def check():
    if arrive[0][0] == arrive[1][1] == arrive[2][2]: return arrive[2][2]
    if arrive[0][2] == arrive[1][1] == arrive[2][0]: return arrive[2][0]

    for l in range(3):
        if arrive[l][0] == arrive[l][1] == arrive[l][2]: return arrive[l][2]

    for c in range(3):
        if arrive[0][c] == arrive[1][c] == arrive[2][c]: return arrive[2][c]

def click(x, y):
    global turn

    line = 1
    column = 1

    if x < X + SPACE: column = 0
    elif x > X + 2*SPACE: column = 2

    if y > Y - SPACE: line = 0
    elif y < Y - 2*SPACE: line = 2

    # ignore click
    if arrive[line][column] != None: return

    # print
    centre_touch_line = (-line*SPACE - SPACE/2) + size/2
    centre_touch_column = (column*SPACE + SPACE/2) - size/2

    xo.penup()
    xo.goto(centre_touch_column-50, centre_touch_line-75)
    if turn == 'x': xo.write('X', font=('Arial',100))
    else: xo.write('O', font=('Arial',100))

    # add to arrive
    arrive[line][column] = turn
    if turn == 'o': turn = 'x'
    else: turn = 'o'

    # check
    if check() != None:
        xo.penup()
        xo.goto(-180, -50)
        time.sleep(0.5)
        xo.clear()
        xo.write("wins " + check(), font=('Arial', 100))


window.onclick(click)

window.listen()         # listen to events
window.mainloop()