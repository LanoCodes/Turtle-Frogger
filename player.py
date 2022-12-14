from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.level = 1

    def move_up(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1
        else:
            self.forward(MOVE_DISTANCE)
