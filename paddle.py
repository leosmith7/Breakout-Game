from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.penup()
        self.goto(position)

    def go_left(self):
        if self.xcor() > -490:
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 490:
            new_x = self.xcor() + 40
            self.goto(new_x, self.ycor())
