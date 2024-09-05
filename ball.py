from turtle import Turtle
class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def increase_speed(self, new_x, new_y):
        if self.x_move < 0:
            if self.x_move > -new_x:
                self.x_move = -new_x
        else:
            if self.x_move < new_x:
                self.x_move = new_x
        if self.y_move < 0:
            if self.y_move > -new_y:
                self.y_move = -new_y
        else:
            if self.y_move < new_y:
                self.y_move = new_y
    def reset_speed(self):
        self.x_move = 3
        self.y_move = 3






