from turtle import *
from random import choice,randint

COLORS = ["#FF577F", "#EF4F4F", "#6155A6", "#FF8C8C", "#EC524B", "#FF75A0"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice=randint(1,6)
        if random_choice==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.y = randint(-250, 250)
            new_car.goto(300, new_car.y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

