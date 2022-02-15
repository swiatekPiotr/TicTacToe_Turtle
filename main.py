import turtle
from little_turtle import Player
import random


class Game():

    def __init__(self):
        self.window = turtle.Screen()

        self.size = 600

        self.window.setup(self.size, self.size)
        self.window.title("Tic Tac Toe")
        self.window.bgcolor('black')

        turn = random.choice(['x', 'o'])

        self.player = Player(self.size, turn)


        self.window.onclick(self.player.click)

        self.draw()

        self.window.listen()  # listen to events
        self.window.mainloop()

    def draw(self):
        self.player.draw()


if __name__ == "__main__":
    Game()