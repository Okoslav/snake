import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("red")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.xcor = random.randint(-280, 280)
        self.ycor = random.randint(-280, 280)
        self.goto(self.xcor, self.ycor)
