from turtle import Screen, Turtle
from paddle import Paddle
from bricks import Brick
from ball import Ball
from scoreboard import Scoreboard
import time
# Create a turtle screen
BALL_STARTING_POSITION = (0, -260)
PADDLE_STARTING_POSITION = (0, -400)
#CEILING_HEIGHT =

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1140, height=900)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(position=PADDLE_STARTING_POSITION)
ball = Ball(position=BALL_STARTING_POSITION)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

all_bricks = []
brick_colours = ['red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow']
colour_speeds = {'red': 4.5, 'orange': 4, 'green': 3.5, 'yellow': 3}
colour_score = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}

x_coordinate = -530
y_coordinate = 230
for row in range(8):
    current_colour = brick_colours[row]
    for column in range(14):
        brick = Brick(position=(x_coordinate, y_coordinate), colour=current_colour)
        all_bricks.append(brick)
        x_coordinate += 80
    y_coordinate -= 30
    x_coordinate = -530

scoreboard.update_scoreboard()


is_game_on = True
while is_game_on:

    screen.update()
    ball.move()
    #Detect Side X wall collision
    if ball.xcor() > 530 + 20 or ball.xcor() < -530 - 20:
        ball.x_bounce()
    #Detect Top ceiling collision
    if ball.ycor() > 265:
        ball.y_bounce()
    #Detect Ball & Paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() < 400:
        ball.y_bounce()
    #Detect if ball hits floor
    if ball.ycor() < -440:
        scoreboard.decrease_lives()
        ball.reset_speed()
        #ball.x_move = ball.x_move * -1
        #ball.y_move = ball.y_move * -1
        time.sleep(3)
        ball.goto(BALL_STARTING_POSITION)
        paddle.goto(PADDLE_STARTING_POSITION)

        if scoreboard.lives == 0:
            is_game_on = False
            scoreboard.game_over()
    #Brick collision
    for brick in all_bricks:
        if ball.distance(brick) < 40:
            #ball.x_bounce()
            brick.hideturtle()
            x_brick, y_brick = brick.position()
            x_ball, y_ball = ball.position()
            x_axis_difference = abs(x_ball - x_brick)
            y_axis_difference = abs(y_ball - y_brick)
            if y_axis_difference > x_axis_difference:
                ball.y_bounce()
            else:
                ball.x_bounce()
            all_bricks.remove(brick)
            scoreboard.increase_score(colour_score[brick.color()[0]])
            new_speed = colour_speeds[brick.color()[0]]
            ball.increase_speed(new_speed, new_speed)
            break

# Close the window on click
screen.exitonclick()

























