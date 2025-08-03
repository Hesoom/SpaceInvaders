from turtle import Screen, Turtle
from random import choice, randint
from ship import Ship
from invader import Invader
from bullet import Bullet
from heart import Heart

# Setup screen
screen = Screen()
screen.bgcolor("#1A1A1A")
screen.setup(width=750, height=650)
screen.title("SpaceInvaders")
screen.tracer(0)
screen.addshape("img/ship.gif")
screen.addshape("img/heart.gif")
screen.addshape("img/invader1.gif")
screen.addshape("img/invader2.gif")
screen.addshape("img/invader3.gif")

# ==== SHIP ====
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

# ==== INVADERS ====
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


# ==== BULLETS ====
bullets = []
bullet_speed = 15
enemy_bullets = []
def shoot():
    bullet = Bullet(ship.position())
    bullets.append(bullet)
screen.onkeypress(shoot, "space")
screen.listen()

create_invaders()

# ==== HP ====
hearts_list = []
hearts = 3
heart_start_x = -280

def reset_hearts():
    global hearts, hearts_list
    for heart in hearts_list:
        heart.hideturtle()
        heart.goto(5000, 5000)
    hearts_list = []

    hearts = 3
    heart_start_x = -280
    for i in range(1, hearts + 1):
        heart = Heart((heart_start_x, 300), "img/heart.gif")
        hearts_list.append(heart)
        heart_start_x += 40

reset_hearts()

game_started = False
def start_game():
    global game_started
    game_started = True

screen.onkeypress(start_game, "Up")


def game_loop():
    global game_started, hearts, hearts_list   
    if game_started:

        move_invaders()

        # Invaders randomly shoot
        if randint(1, 20) == 1:
            shooter = choice(invaders) # A random invader
            bullet = Bullet(shooter.position())
            bullet.setheading(270) # bullet go down
            bullet.color("red")
            enemy_bullets.append(bullet)

        for bullet in enemy_bullets[:]:
            bullet.move_down(bullet_speed)
            
                
            # Ship get hit and detect collision
            if bullet.detect_ship_hit(ship,enemy_bullets,bullets):
                game_started = False
                if hearts > 1:                  
                    hearts -= 1
                    # remove one heart icon
                    lost_heart = hearts_list.pop()  
                    lost_heart.hideturtle()
                    lost_heart.goto(1000, 1000)
                else:
                    reset_hearts()
                
            # Bullet misses
            if bullet.is_off_screen_bottom():
                bullet.hideturtle()
                enemy_bullets.remove(bullet)

        # Move bullets
        for bullet in bullets[:]:
            bullet.move(bullet_speed)
            for invader in invaders[:]:
                # Invader get hit and detect collision
                bullet.detect_invader_hit(invader,invaders)

            # Bullet miss
            if bullet.is_off_screen():
                bullet.hideturtle()
                bullets.remove(bullet)

        if right_pressed:
            ship.move(direction=1)
        if left_pressed:
            ship.move(direction=-1)



    screen.update()
    screen.ontimer(game_loop, 16)

game_loop()
screen.mainloop()
