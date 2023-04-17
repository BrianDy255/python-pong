from turtle import Turtle

class Border_top(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.goto(300,300)
        self.shapesize(0.5,100,0)
        self.color('white')

class Border_bottom(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.goto(300,-300)
        self.shapesize(0.5,100,0)
        self.color('white')


