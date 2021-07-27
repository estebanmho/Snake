from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.change_place()

    def change_place(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        coord = (x_random, y_random)
        self.goto(coord)