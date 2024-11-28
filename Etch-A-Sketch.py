import turtle

print("You can press:")
print("'W' for Forwards, 'S' for Backwards, 'A' for Counter-Clockwise, 'D' for Clockwise, 'C' for Clear drawing")

def move_forwards():
    timmy.forward(20)
    
def move_backwards():
    timmy.backward(20)

def move_left():
    timmy.left(10)

def move_right():
    timmy.right(10)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen = turtle.Screen()       
timmy = turtle.Turtle()

screen.listen()
screen.onkey( move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()