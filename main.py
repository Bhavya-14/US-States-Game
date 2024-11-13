import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

states = pandas.read_csv('50_states.csv')
no_of_states = 50
states_guessed = 0
guessed_states = []


while True:
    answer = turtle.textinput(title=f'{states_guessed}/{no_of_states} states guessed', prompt='What\'s another '
                                                                                              'state\'s name?').title()
    if answer in states.state.values and answer not in guessed_states:
        guessed_states.append(answer)
        x_cor = states.loc[states.state == answer, 'x'].values[0]
        y_cor = states.loc[states.state == answer, 'y'].values[0]
        correct_state = turtle.Turtle()
        correct_state.penup()
        correct_state.hideturtle()
        correct_state.goto(int(x_cor), int(y_cor))
        correct_state.write(arg=answer, font=('Arial', 10, 'bold'))
        states_guessed += 1
    if states_guessed == 50:
        turtle.write('You\'ve Guessed All States!', align='Center', font=('Arial', 30, 'normal'))
        break
turtle.mainloop()
