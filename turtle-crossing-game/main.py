import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
# init screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# create our classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
# listen
screen.listen()
screen.onkey(key="Up", fun=player.move)
# start the game
game_is_on = True
while game_is_on:
    car_manager.add_car()
    car_manager.move()
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level_up()
        player.reset_position()
        car_manager.level_up()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
    time.sleep(0.1)
    screen.update()
# end the game
scoreboard.game_over()
screen.exitonclick()
