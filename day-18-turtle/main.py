import turtle
from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, g, b

def circle_space(space):
    for _ in range(int(360/space)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + space)


turtle.colormode(255)

DIRECTION = [0, 90, 180, 270]

tim = Turtle()
tim.speed("fastest")
my_screen = Screen()
red = random.randint(0, 255)
blue = random.randint(0, 255)
green = random.randint(0, 255)

circle_space(25)

# for i in range(3, 11):
#     tim.color(random.choice(COLORS))
#     for _ in range(i):
#         tim.right(360 / i)
#         tim.forward(100)

# for _ in range(200):
#     angle = random.choice(DIRECTION)
#     tim.color(random_color())
#     tim.setheading(angle)
#     tim.forward(10)




my_screen.exitonclick()
