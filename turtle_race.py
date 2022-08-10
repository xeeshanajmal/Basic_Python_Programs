import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the Race?  Enter a color:")
color = ["red", "green", "blue", "black", "orange", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won and the {winning_color} turtle is the winner.")
            else:
                print(f"You have LOST and the {winning_color} turtle is the winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
