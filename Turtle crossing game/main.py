from turtle import Screen
from Turtle import Create_turtle
from cars import Create_car
from scoreboard import Score

from time import sleep

screen = Screen()
screen.setup(height=600, width=600)

screen.tracer(0)

mc = Create_turtle()
mc.goto(x=0,y=-200)

score = Score()

screen.listen()
screen.onkeypress(fun=mc.move_forward,key="Up")

cars = []

for _ in range(50):
    car = Create_car()
    car.colored_cars()
    cars.append(car)


game_is_on = True
i = 0
score.levelup(i)
while game_is_on:
    
    for car in cars:
        car.move_car()
        if car.xcor()>300:
            car.end()

        if mc.distance(car)<20:
            gameover = Create_turtle()
            gameover.hideturtle()
            gameover.write("Game Over", align="center",font=("Bold", 50, "normal"))
            game_is_on = False

    if mc.ycor()>200:
        i=i+1
        score.clear()
        score.levelup(i)
        mc.goto(x=0,y=-200)


    sleep(0.01)
    screen.update()    

screen.exitonclick()