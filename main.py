from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from functools import partial

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()

screen.listen( )
screen.update()
gameIsON = True
def end_game(game):
    game=False
func = partial(end_game, gameIsON)
screen.onkeypress(key="Right",fun=snake.move_right)
screen.onkeypress(key="Left",fun=snake.move_left)
screen.onkeypress(key="Up",fun=snake.move_up)
screen.onkeypress(key="Down",fun=snake.move_down)
screen.onkeypress(key="q", fun=func)

food = Food()
scoreboard1 = ScoreBoard()
while gameIsON:
    snake.move(screen)
    if snake.head.distance(food.position()) < 15:
        food.change_place()
        snake.add_segment()

        scoreboard1.update_score()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard1.reset()
        snake.reset()
    for segment in snake.snake[1:]:
        if segment.distance(snake.head)<10:
            scoreboard1.reset()
            snake.reset()

snake.hide()
screen.update()

screen.exitonclick()


