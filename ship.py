from turtle import Turtle

class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.start_position = position
        self.penup()
        self.goto(self.start_position)
        self.shape("img/ship.gif")        
        self.shapesize(stretch_wid=1, stretch_len=2)
        
    def reset(self):
        self.goto(self.start_position)

    def move(self, direction):
        step = 10
        new_x = self.xcor() + direction * step
        if -280 < new_x < 280:
            self.goto(new_x, self.ycor())

