import turtle
from turtle import Turtle
screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gia-Khanh-Snake-Game")
starting_position={(-40,0),(-20,0),(0,0)}
for i in starting_position:
    body=Turtle("square")
    body.color("white")
    body.goto(i)
    
screen.exitonclick()