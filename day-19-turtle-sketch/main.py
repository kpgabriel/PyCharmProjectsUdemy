import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(height=400, width=500)

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
i = 0
y = -100


for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 25
    i += 1

user_bet = screen.textinput("Bet", "Which turtle do you think will win? ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet.lower() == winning_color:
                print(f"{winning_color} Wins!!! Good Bet!")
            else:
                print(f"Sorry the winning turtle was {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
