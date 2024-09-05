from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, colour):
        super().__init__()
        self.color(colour)
        self.shape("square")
        self.shapesize(stretch_len=3.5, stretch_wid=0.75)
        self.penup()
        self.goto(position)
