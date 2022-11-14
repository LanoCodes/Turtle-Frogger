from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("black")
        self.hideturtle()
        self.goto(-230, 270)

    def update_score(self, level):
        self.clear()
        self.write(f"Level: {level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
