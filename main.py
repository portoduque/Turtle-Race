from turtle import Turtle, Screen
from layout import Layout

import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Create layout
layout = Layout()
layout.draw_end_flag()

# Create Turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_position = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    new_turtle.color(colors[turtle_index])

    all_turtle.append(new_turtle)

    y_position += 40

# Check if the user bet was successful
if user_bet:
    is_race_on = True

# Start race
while is_race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0, 8)
        turtle.forward(random_distance)

        # Check if turtle cross the end flag
        if turtle.xcor() > 190:
            is_race_on = False
            winner_color = turtle.pencolor()

            # Check if the user wins
            if user_bet == winner_color:
                layout.victory(winner_color)
            else:
                layout.defeat(winner_color)

screen.exitonclick()
