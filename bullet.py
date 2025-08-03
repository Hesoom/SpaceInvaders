from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("yellow")
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.goto(position)
        self.setheading(90)  # Point up

    def move(self, speed=10):
        new_y = self.ycor() + speed
        self.goto(self.xcor(), new_y)

    def is_off_screen(self):
        return self.ycor() > 300
    
    def move_down(self, speed=10):
        new_y = self.ycor() - speed
        self.goto(self.xcor(), new_y)

    def is_off_screen_bottom(self):
        return self.ycor() < -300
    
    def reset(self):
        self.goto((5000,5000))

    def detect_invader_hit(self,invader,invaders_list):
        if (
            abs(self.xcor() - invader.xcor()) < 40 and
            abs(self.ycor() - invader.ycor()) < 20
        ):
            invaders_list.remove(invader)
            invader.die()
            self.reset()
        
    def detect_ship_hit(self,ship,enemy_bullets,bullets):
        if (
            abs(self.xcor() - ship.xcor()) < 40 and
            abs(self.ycor() - ship.ycor()) < 20
        ):
            ship.reset()
            for bullet in enemy_bullets[:]:
                enemy_bullets.remove(bullet)
                bullet.reset()
            for bullet in bullets[:]:
                bullets.remove(bullet)
                bullet.reset()

            return True