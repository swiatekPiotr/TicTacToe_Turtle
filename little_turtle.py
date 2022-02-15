import turtle
from checking import check
import time


class Player():

    def __init__(self, size, turn):
        self.size = size
        self.X = -self.size / 2
        self.Y = self.size / 2

        self.arrive = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

        self.turn = turn

        self.xo = turtle.Turtle()

        self.SPACE = self.size / 3


    def click(self, x, y):

        line = 1
        column = 1

        if x < self.X + self.SPACE:
            column = 0
        elif x > self.X + 2 * self.SPACE:
            column = 2

        if y > self.Y - self.SPACE:
            line = 0
        elif y < self.Y - 2 * self.SPACE:
            line = 2

        # ignore click
        if self.arrive[line][column] != None: return

        # print
        centre_touch_line = (-line * self.SPACE - self.SPACE / 2) + self.size / 2
        centre_touch_column = (column * self.SPACE + self.SPACE / 2) - self.size / 2

        self.xo.penup()
        self.xo.goto(centre_touch_column - 50, centre_touch_line - 75)
        if self.turn == 'x':
            self.xo.write('X', font=('Arial', 100))
        else:
            self.xo.write('O', font=('Arial', 100))

        # add to arrive
        self.arrive[line][column] = self.turn
        if self.turn == 'o':
            self.turn = 'x'
        else:
            self.turn = 'o'

        # check
        if check(self.arrive) != None:
            self.xo.penup()
            self.xo.goto(-180, -50)
            time.sleep(0.5)
            self.xo.clear()
            self.xo.write("wins " + check(self.arrive), font=('Arial', 100))


    def draw(self):
        self.xo.color('white')
        self.xo.pensize(8)
        self.xo.speed(0)
        self.xo.hideturtle()

        for a in [1, 2]:
            self.xo.penup()
            self.xo.goto(self.X + a * self.SPACE, self.Y)
            self.xo.pendown()
            self.xo.goto(self.X + a * self.SPACE, -self.Y)

            self.xo.penup()
            self.xo.goto(self.X, self.Y - a * self.SPACE)
            self.xo.pendown()
            self.xo.goto(-self.X, self.Y - a * self.SPACE)