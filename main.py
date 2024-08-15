import turtle
from turtle import Turtle
import time
screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gia-Khanh-Snake-Game")
starting_position={(0,0),(-20,0),(-40,0)}
run=[]
screen.tracer(0)
for i in starting_position:
    body=Turtle("square")
    body.color("white")
    body.penup()
    body.goto(i)
    run.append(body)
screen.update()
while True:
    screen.update()
    time.sleep(0.1)
    for i in range(2,0,-1):
        new_x=run[i-1].xcor()
        new_y=run[i-1].ycor()
        run[i].goto(new_x,new_y)
    run[0].forward(20)
    run[0].left(90)

exitonclick()