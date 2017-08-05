import turtle
def menu():
    x = input('would you like to start the game? \n (YES/NO) \n would you like to quit the menu bar? \n (QUIT) \n *PLEASE USE CAPITAL LETTERS \n YOUR ANSWER: ')
    if x == 'NO' or x == 'QUIT':
        quit()
    elif x == 'YES':
        print('')

menu()

turtle.penup()
#bird = turtle.clone()
#turtle.addshape('bird.gif')
#bird.shape('bird.gif')
turtle.shape('circle')
#turtle.hideturtle()
turtle.Screen()
screen = turtle.Screen()
screen.bgcolor('light blue')

turtle.goto(0,-300)

box_pos=[]
bird_pos=[]

#turtle.setup(400,400)

my_pos = turtle.pos()

x_pos = my_pos[0]
y_pos = my_pos[1]
UP_EDGE = -200
DOWN_EDGE = -400
RIGHT_EDGE = 100
LEFT_EDGE = -100

'''
while True:
    x_pos < RIGHT_EDGE
    x_pos > LEFT_EDGE
    y_pos < UP_EDGE
    y_pos > DOWN_EDGE
'''
UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100
SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

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

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
    



def move_bird():
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction == RIGHT:
        turtle.goto(x_pos + 10,y_pos)
    elif direction == LEFT:
        turtle.goto(x_pos - 10,y_pos)
    elif direction == UP:
        turtle.goto(x_pos, y_pos + 10)
    elif direction == DOWN:
        turtle.goto(x_pos, y_pos -10)
        
    turtle.ontimer(move_bird,TIME_STEP)

def box():
    box = turtle.clone()
    
    #box.addshape('box.gif')
    #box.shape('box.gif')
    box.shape('square')
    
move_bird()
