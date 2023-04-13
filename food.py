from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))

    def new_location(self):
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))