import turtle
turtle.penup()
bird = turtle.clone()
turtle.addshape('bird.gif')
bird.shape('bird.gif')
turtle.hideturtle()
turtle.Screen()
screen = turtle.Screen()
screen.bgcolor('light blue')

bird.goto(0,-250)


box_pos=[]
bird_pos=[]

turtle.setup(600,600)





def move_bird():
    bird.pos()
    x_pos = bird.pos()[0]
    y_pos = bird.pos()[1]
    my_pos = bird.pos()
    my_pos(x_pos,y_pos)
    bird_pos.append(my_pos)


    UP= 0
    DOWN = 2
    LEFT = 1
    RIGHT= 3
    direction = UP

def up():
    global direction
    direction = UP
    print('you pressed the up key')
    
def down():
        global direction
        direction = DOWN
        print('you pressed the down key')
    
def left():
        global direction
        direction = LEFT
        print('you pressed the left key')
    
def right():
    global direction
    direction = RIGHT
    print('you pressed the right key')



UP_ARROW = 'UP'
DOWN_ARROW = 'DOWN'
LEFT_ARROW = 'LEFT'
RIGHT_ARROW ='RIGHT'

turtle.onkeypress(up, UP_ARROW)
bird.onkeypress(down, DOWN_ARROW)
bird.onkeypress(left, LEFT_ARROW)
bird.onkeypress(right, RIGHT_ARROW)
bird.listen()

bird_pos[-1].clearstamp()
bird_pos[-1].pop()

