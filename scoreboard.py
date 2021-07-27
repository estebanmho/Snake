from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        file = open("data.txt")
        self.score=0
        super().__init__()
        self.high_score = int(file.read())
        file.close()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score} High score {self.high_score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.show_score()

    def reset(self):
        if self.score> self.high_score:
            file = open("data.txt", mode="w")
            file.write(str(self.score))
            file.close()
            self.high_score = self.score
        self.score = 0
        self.update_score()

