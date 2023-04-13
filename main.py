from turtle import Turtle, Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='My Snake Game')
screen.colormode(255)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()
screen.listen()



is_game_on = True
while is_game_on:
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.segments[0].distance(food) < 15:
        print("Ate the food")
        scoreboard.increment_score()
        snake.make_snake_bigger()
        food.new_location()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()
        screen.update()
        #break

    if snake.hit_body():
        scoreboard.reset()
        snake.reset()
        screen.update()
        #break

    

















screen.exitonclick()