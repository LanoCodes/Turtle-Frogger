from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# car_placement = random.randint(-250, 250)

class CarManager(Turtle):

    # def __init__(self, y_coord):
    def __init__(self):
        # super().__init__()
        # self.penup()
        # self.color(random.choice(COLORS))
        # self.shape("square")
        # self.setheading(180)
        # self.shapesize(stretch_wid=1, stretch_len=2)
        # self.goto(310, y_coord)
        # self.drive()

        self.all_cars = []

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            car_placement = random.randint(-250, 250)
            new_car.goto(300, car_placement)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)