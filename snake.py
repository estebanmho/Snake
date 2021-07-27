from turtle import Turtle, Screen
import time
UP=90
DOWN=270
RIGHT=0
LEFT=180
STEP_DISTANCE=20

class Snake:

    def __init__(self):
        self.snake = []
        for i in range(3):
           self.add_tail((0 - i * 20,0))
        self.head = self.snake[0]

    def move(self,screen):
        for seg in range(len(self.snake) - 1, -1, -1):  # El final no se incluye por eso el -1
            if seg != 0:
                self.snake[seg].goto(self.snake[seg - 1].position())
            else:
                self.head.forward(STEP_DISTANCE)
        screen.update()
        time.sleep(0.2)

    def starting_snake(self):
        for i in range(3):
           self.add_tail((0 - i * 20,0))
        self.head = self.snake[0]

    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def add_tail(self):
        if self.snake[len(self.snake)-1].xcor():
            print("!")

    def hide(self):
        for turtle in self.snake:
            turtle.hideturtle()

    def add_tail(self, position):
        turtle = Turtle(shape="square")
        turtle.color("White")
        turtle.penup()
        turtle.speed("fastest")
        turtle.setposition(position)
        self.snake.append(turtle)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.starting_snake()
    def add_segment(self):
        self.add_tail(self.snake[-1].position())