from turtle import Turtle

class Heart(Turtle):
    def __init__(self, position, heart_shape):
        super().__init__()
        self.shape(heart_shape)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(position)