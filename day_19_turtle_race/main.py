from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1000,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
step = [5,8,10]
color = ["red","IndianRed","yellow","green","blue","orange","purple"]
y_position = [-70, -40, -10, 20, 50, 80, 110]

all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.goto(x = -480, y = y_position[turtle_index])
    new_turtle.color(color[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 460:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()     
