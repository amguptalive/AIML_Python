from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
is_race_on = False
all_turtles = []
print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color != user_bet:
                print(f"You've lost! The {winning_color} is the winner!")
            else:
                print(f"You've won! The {winning_color} is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        turtle.speed("fastest")
# tony = Turtle(shape="turtle")
# tony.penup()
# tony.color(colors[4])
# tony.goto(x=-230, y=60)
#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color(colors[3])
# tom.goto(x=-230, y=20)
#
# timmy = Turtle(shape="turtle")
# timmy.penup()
# timmy.color(colors[2])
# timmy.goto(x=-230, y=-20)
#
# binny = Turtle(shape="turtle")
# binny.penup()
# binny.color(colors[1])
# binny.goto(x=-230, y=-60)
#
# jon = Turtle(shape="turtle")
# jon.penup()
# jon.color(colors[0])
# jon.goto(x=-230, y=-100)

screen.listen()

screen.exitonclick()
