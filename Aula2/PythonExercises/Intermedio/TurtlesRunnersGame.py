from turtle import Turtle, Screen
import random

run = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Carrera", 'Cuál tortuga ganará la carrera? Ingrese un color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
pos_y = [125, 75, 25, -25, -75, -125]

turtles = []
for turtle_index in range(0,6):
    turtles.append(Turtle('turtle'))
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].penup()
    turtles[turtle_index].goto(-230,pos_y[turtle_index])

if user_bet:
    run = True
while run == True:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            if turtle.color() == user_bet:
                print(f'Usted ganó, la tortuga {turtle.pencolor()} es la ganadora')
            else:
                print(f'Usted perdió, la tortuga {turtle.pencolor()} es la ganadora')
            run = False
            break

screen.exitonclick()