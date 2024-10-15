import argparse
import time
import turtle
import random

class Koch:

    def __init__(self, level):
        level = int(level)
        if level <= 0 or level > 12:
            raise Exception("Level must be between 1 and 12")

        self.max_level = level
        self.screen = None
        self.board = None
        self.position = 0
        self.base_line_length = 300
        self.__initialize_turtle()

    def __initialize_turtle(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1.0, height=1.0)  # Note that it needs to be 1.0, and not 1
        screensize = self.screen.screensize()
        turtle.colormode(255)
        #turtle.tracer(0)
        turtle.hideturtle()
        self.board = turtle.Turtle()
        self.board.speed(0)
        self.position = -screensize[0]
        self.board.up()
        self.board.setpos(0, -screensize[1])
        self.board.down()

    def __leaf(self, level, line_length):
        self.board.forward(line_length)
        if level > 0:
            self.board.right(45)
            self.__draw(level - 1, line_length * 2 // 3)
            self.board.right(45)
        self.board.forward(-line_length)

    def __draw(self, level, line_length):
        self.__leaf(level, line_length)
        self.board.left(90)
        self.__leaf(level, line_length)

    def show(self):

        self.board.left(90)
        self.board.forward(self.base_line_length)
        self.board.right(45)

        self.__draw(self.max_level, self.base_line_length * 2 // 3)

        turtle.done()
        self.screen.exitonclick()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level", help="Level of fractal. Max=12", default=8)
    args = parser.parse_args()
    koch = Koch(level=args.level)
    koch.show()

