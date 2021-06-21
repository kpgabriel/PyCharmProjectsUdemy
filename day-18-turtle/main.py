from turtle import Turtle,Screen

tim = Turtle()
my_screen = Screen()

#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Drawing shapes.
for _ in range(3):
    tim.right(360 / 3)
    tim.forward(100)


my_screen.exitonclick()
