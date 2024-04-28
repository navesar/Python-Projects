from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.turtlesize(stretch_len=2)
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300, y=random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def level_up(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
        self.move_distance += MOVE_INCREMENT
