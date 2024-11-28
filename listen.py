from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move():
    timmy.forward(20)

screen.onkey(key="space", fun = move)

screen.listen()
screen.exitonclick()