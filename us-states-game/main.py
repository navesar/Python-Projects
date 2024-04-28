from turtle import Turtle, Screen
import pandas


def next_guess(cor_ans):
    curr_guess = screen.textinput(title=f"{cor_ans}/50 Correct", prompt="Enter another state's name:")
    return curr_guess.title() if curr_guess is not None else curr_guess


# init screen
screen = Screen()
screen.setup(width=720, height=490)
screen.title("US States Game")
# init turtle
img = "blank_states_img.gif"
screen.addshape(img)
map_turtle = Turtle(shape=img)
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")
# init data
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
# start game
while len(guessed_states) < 50:
    guess = next_guess(len(guessed_states))
    if guess == "Exit" or guess is None:
        break
    elif guess in states:
        guessed_states.append(guess)
        xcor = data[data["state"] == guess]["x"].values[0]
        ycor = data[data["state"] == guess]["y"].values[0]
        writer.goto(xcor, ycor)
        writer.write(arg=guess)
screen.exitonclick()  # game over
# export states to learn
states_to_learn = [state for state in states if state not in guessed_states] 
df = pandas.DataFrame({"States to learn": states_to_learn})
df.to_csv("states_to_learn.csv")
