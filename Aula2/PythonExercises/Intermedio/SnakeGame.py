from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)
starting_positions= [(0,0), (-20,0), (-40,0)]

snake = []

for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(positions)
    snake.append(new_segment)

game = True
flag = True

while game:
    screen.update()
    time.sleep(0.1)
    for seg in snake:
        for seg_num in range(len(snake)-1,-1,-1):
            if seg_num == 0:
                if flag:
                    snake[seg_num].left(90)
                    flag = False
                
            else:
                snake[seg_num].goto(snake[seg_num-1].pos())
    




    
        
        
    


screen.exitonclick()