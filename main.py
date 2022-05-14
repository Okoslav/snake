from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import pytest

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Had :-)")
screen.tracer(n=0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()

game_is_on = True
food = Food()

while game_is_on:

    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.make_snake_longer()

    if snake.head.xcor() >= 300:
        scoreboard.reset()
        snake.reset()

    if snake.head.ycor() >= 300:
        scoreboard.reset()
        snake.reset()

    if snake.head.xcor() <= -300:
        scoreboard.reset()
        snake.reset()

    if snake.head.ycor() <= -300:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()






















screen.exitonclick()