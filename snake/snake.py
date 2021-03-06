import turtle
import random

turtle.tracer(1,0)

turtle.penup()
score1 = turtle.clone()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food.hideturtle()

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)



SQUARE_SIZE = 20
START_LENGTH = 6
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape('square')
turtle.bgcolor('lightblue')
snake.fillcolor('blue')
turtle.hideturtle()

for START_LENGTH in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos += SQUARE_SIZE

    my_pos = (x_pos,y_pos)
    snake.goto(x_pos, y_pos)

    pos_list.append(my_pos)

    stamp = snake.stamp()
    stamp_list.append(stamp)
    

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
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
x = 0
score1.hideturtle()
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
turtle.onkeypress(turtle.stamp, SPACEBAR)
turtle.listen()

def make_food():
    #turtle.penup()
    global food_stamps,food_pos,food
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    stampnew = food.stamp()
    food_stamps.append(stampnew)
    #turtle.pendown()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE,y_pos)
        
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    global food_stamps,food_pos,x
    
    if not snake.pos() in food_pos:
        my_pos = snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    elif snake.pos() in food_pos:
        my_pos = snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)        
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food')
        make_food()
        x =  x + 1
        score1.goto(0,0)
        score1.clear()
        score1.write('SCORE:' + str(x), False, "left", ("Arial", 16, "normal"))
    else:
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food')
        make_food()
    
    
            
   
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >=RIGHT_EDGE:
        print('you hit the right edge!game over!')
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print('you hit the left edge!game over!')
        quit()
    elif new_y_pos >= UP_EDGE:
        print('you hit the up edge!game over!')
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print('you hit the down edge!game over!')
        quit()

    if new_pos in pos_list[0:-1]:
        print('you eat yourself!game over')
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

        
make_food()
move_snake()

'''
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
food.hideturtle()

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    f=food.stamp()
    food_stamps.append(f)

'''
    
