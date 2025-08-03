from turtle import Screen, Turtle
from ship import Ship
from invader import Invader

# Setup screen
screen = Screen()
screen.bgcolor("#1A1A1A")
screen.setup(width=750, height=650)
screen.title("SpaceInvaders")
screen.tracer(0)
screen.addshape("img/invader1.gif")
screen.addshape("img/invader2.gif")
screen.addshape("img/invader3.gif")

ship = Ship(position=(0,-250))

right_pressed = False
left_pressed = False

def hold_right():
    global right_pressed
    right_pressed = True

def release_right():
    global right_pressed
    right_pressed = False

def hold_left():
    global left_pressed
    left_pressed = True

def release_left():
    global left_pressed
    left_pressed = False

screen.listen()
screen.onkeypress(hold_right, "Right")
screen.onkeyrelease(release_right, "Right")
screen.onkeypress(hold_left, "Left")
screen.onkeyrelease(release_left, "Left")

# Creating Invaders
invaders = []
start_x = -260
start_y = 250
rows = 5
columns = 11
x_spacing = 50
y_spacing = 50
shapes = ["img/invader1.gif","img/invader2.gif","img/invader3.gif"]
index = 0
invader_direction = 1
invader_speed = 1      
invader_step_down = 20

def create_invaders():
    global invaders, index
    for invader in invaders:
        invader.hideturtle()
        invader.goto(1000, 1000)  # Move them offscreen just in case
    invaders = []  # Clear the old list

    for row in range(rows):
        for col in range(columns):
            x = start_x + col * x_spacing
            y = start_y - row * y_spacing
            shape = shapes[index % len(shapes)]
            index += 1
            invader = Invader(position=(x, y),shape=shape)
            invaders.append(invader)

invader_direction = 1
invader_speed = 1      
invader_step_down = 5

def move_invaders():
    global invader_direction
    edge_hit = False

    for invader in invaders:
        next_x = invader.xcor() + invader_direction * invader_speed
        if next_x > 310 or next_x < -310:
            edge_hit = True
            break  

    if edge_hit:
        invader_direction *= -1
        for invader in invaders:
            invader.drop_down(invader_step_down)
    else:
        for invader in invaders:
            invader.move(invader_direction, invader_speed)

create_invaders()

game_started = False
def start_game():
    global game_started
    game_started = True

screen.onkeypress(start_game, "Up")

def game_loop():
    global game_started
    if game_started:

        move_invaders()


        if right_pressed:
            ship.move(direction=1)
        if left_pressed:
            ship.move(direction=-1)


    screen.update()
    screen.ontimer(game_loop, 16)

game_loop()
screen.mainloop()
