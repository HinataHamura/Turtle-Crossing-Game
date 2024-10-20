import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("#E5D4FF")
screen.tracer(0)

plaayer = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(plaayer.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    #detect collision with cars
    for cars in car.all_cars:
        if cars.distance(plaayer)< 25:
            game_is_on = False
            score.game_over()

    #reach top edge
    if plaayer.ycor() > 280:
        plaayer.go()
        car.level_up()
        score.increase_level()






screen.exitonclick()
