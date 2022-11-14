import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Frogger")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
score_keeper = player.level

speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()

    car_manager.make_car()
    car_manager.move_car()

    if player.level > score_keeper:
        score_keeper = player.level
        car_manager.drive_faster()
        speed *= 0.6
        print(speed)

    # Detecting whether a car has hit the turtle
    collision_detected = True in (player.distance(ele) < 24 for ele in car_manager.all_cars)
    if collision_detected:
        scoreboard.game_over()
        game_is_on = False
    else:
        scoreboard.update_score(player.level)

screen.exitonclick()
