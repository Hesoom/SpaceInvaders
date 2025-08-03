from turtle import Turtle

class Invader(Turtle):
    def __init__(self, position,shape):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape(shape)
        self.goto(position)
        self.x_move = 1

    def move(self, direction, step=1):
        new_x = self.xcor() + direction * step
        self.goto(new_x, self.ycor())

    def drop_down(self, distance=5):
        new_y = self.ycor() - distance
        self.goto(self.xcor(), new_y)