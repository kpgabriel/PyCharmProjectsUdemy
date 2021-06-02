from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

tim.shape("classic")
for _ in range(4):
    tim.forward(100)
    tim.right(90)


my_screen.exitonclick()
