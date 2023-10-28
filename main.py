from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_position = [(0,0), (-20,0), (-40,0)]

for position in starting_position:
    kaa = Turtle(shape="square")
    kaa.color("white")
    kaa.penup()
    kaa.goto(position)




screen.exitonclick()