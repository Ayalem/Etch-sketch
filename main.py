import turtle as t
from turtle import Turtle,Screen
tim=t.Turtle()
screen=Screen()
screen.listen()
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_CounterClockwise():
  tim.setheading(tim.heading()+10)

def move_Clockwise():
    tim.setheading(tim.heading()-10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=move_CounterClockwise,key="a")
screen.onkey(fun=move_Clockwise,key="d")
screen.onkey(fun=clear_drawing,key="c")
screen.exitonclick()
















