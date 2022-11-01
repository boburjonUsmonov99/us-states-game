import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",  prompt = "What is another states name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        final = turtle.Turtle()
        final.hideturtle()
        final.penup()
        final.goto(0,0)
        final.write(missing_states)
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)



