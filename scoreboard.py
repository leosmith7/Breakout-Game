from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.width(10)

        self.lives = 3
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-570, 350)
        self.pendown()
        self.forward(1150)
        self.penup()
        self.goto(0, 380)
        self.write(f"Score: {self.score} | Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))
        self.penup()


    def increase_score(self, score):
        self.score += score
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.color('red')
        self.write('GAME OVER', align="center", font=("Courier", 110, 'bold'))




















