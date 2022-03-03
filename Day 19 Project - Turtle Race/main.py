from turtle import Turtle, Screen
import random

screen = Screen()
# screen.screensize(canvwidth=1000, canvheight=400)

screen.setworldcoordinates(llx=0, lly=0, urx=800, ury=200)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racing_turtles = []

for n in range(6):
    turt = Turtle(shape="turtle")
    turt.shapesize(3)
    turt.color(turtle_colors[n])
    turt.penup()
    turt.goto(x=10, y=(50 + (n*20)))
    racing_turtles.append(turt)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will "
"win the race? Enter a color: ")

do_race = True
while do_race:
    for turtle in racing_turtles:
        if turtle.xcor() > 770:
            do_race = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                screen.title("Your turtle won!!! Congratulations!!!")
            else:
                screen.title(f"Your turtle lost!!! The winner was the "
                      f"{winner_color} turtle!!!")
        turt_move = random.randint(0,10)
        turtle.forward(turt_move)

screen.exitonclick()
