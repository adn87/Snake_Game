import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in starting_position:
    kaa = Turtle(shape="square")
    kaa.color("white")
    kaa.penup()
    kaa.goto(position)
    snake.append(kaa)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # range (start = len(snake) -1, stop = 0, step = -1)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()
