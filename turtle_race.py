import turtle
import random


screen = turtle.Screen() 

screen.setup (width=500, height=400)
user_bet =  screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles= []
for index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x= -240, y= y_positions[index])
    all_turtles.append(new_turtle)
    
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won the bet!")
            else:
                print(f"The {winning_color} turtle won! You lost the bet!")
            print(turtle.color())
        my_distance = random.randint(0,10)
        turtle.forward(my_distance)
     


screen.exitonclick()