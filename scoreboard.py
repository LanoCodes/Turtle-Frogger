from turtle import Turtle
from player import Player

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("black")
        self.hideturtle()
        self.goto(-230, 270)

    def update_score(self):
        self.write(f"Level: X", move=False, align="center", font=FONT)