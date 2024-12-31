import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_list = []

# 2 - Check if guess is among 50 states
df = pd.read_csv('50_states.csv')
all_states = df.state.to_list()
score = 0
# 4 - Use a loop to allow the user to keep guessing
while len(guessed_list) < 50:

    # 6 - Keep track of score
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()  # 1 - Convert the guess to Title
    # case
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #    if state not in guessed_list:
        #        missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_list.append(answer_state)  # 5 - Record the correct guesses in list
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))

        # 3 - Write correct guesses onto the map
        # t.write(state_data.state.item()) or
        t.write(answer_state)


