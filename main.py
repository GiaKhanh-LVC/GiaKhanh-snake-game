import turtle
from turtle import Turtle
screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gia-Khanh-Snake-Game")
starting_position={(-40,0),(-20,0),(0,0)}
run=[]
for i in starting_position:
    body=Turtle("square")
    body.color("white")
    body.tracer(8,25)
    body.penup()
    body.goto(i)
    run.append(body)
while True:
    for i in run:
        i.update()
        i.tracer(8,25)    
        i.penup()
        i.forward(20)
        
screen.exitonclick()