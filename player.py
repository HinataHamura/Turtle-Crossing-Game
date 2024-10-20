from turtle import *
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("indianred")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    # def restart(self):
    #     self.goto(0,0)
    #     self.hideturtle()
    #     self.color("#9A208C")
    #     self.write("REACHED FINISH LINE!!",align="center",font=("Courier", 30, "bold"))
    #     time.sleep(2)


    def go(self):
        self.goto(STARTING_POSITION)
        # self.showturtle()



