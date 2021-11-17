# import turtle module
import turtle
# import pandas module
import pandas
# TODO create screen object with Screen class
screen = turtle.Screen()
# change title
screen.title("U.S. State Guess Game")
# TODO load in new image as new shape
# image variable to store file path name
img = "blank_states_img.gif"
screen.addshape(img)
# once image added to screen turtle can access it
turtle.shape(img)
# # mouse click function return x and y coordinates---------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
# # event listener
# turtle.onscreenclick(get_mouse_click_coor)
# -----------------------------------------------------------------------------
# pandas read csv file
data = pandas.read_csv("50_states.csv")

# TODO Prompt user for input
# data series stored in all_states variable
all_states = data["state"].to_list()
# empty list to store correct guesses
guessed_states = []
# loop to prompt user until all guessed states = 50
while len(guessed_states) <= 50:
    # turtle input stored in variable
    # title function to edit string
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 Correct States", prompt="Whats another state name? ").title()
    # Exit answer is given terminate
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        if answer_state == "Exit":
            missing_states = [
                state for state in all_states if state not in guessed_states]

        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # use in to check for membership in all_states list
    if answer_state in all_states:
        # append guessed state to guessed states list
        guessed_states.append(answer_state)
        # construct new turtle object
        t = turtle.Turtle()
        t.hideturtle()
        # avoid drawing to increase performance
        t.penup()
        # get a hold of row of data
        state_data = data[data["state"] == answer_state]
        # navigate to location in turtle screen
        t.goto(int(state_data.x), int(state_data.y))
        # write name of state state_data["state"] is the same as below
        t.write(state_data.state.item())
