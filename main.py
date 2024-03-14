from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Ruth's Snake Game")
# turn off tracer:
screen.tracer(0)  # Turn off animation updates

snake = Snake()
#The function that you're going to bind it to is going to be a function in the
#snake object and it's going to have the same name. going to call methods in snake class.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# create new snake object from class
# And once this line gets triggered, then we're going to be calling
# create_snake and our three-segment snake will show up on screen
snake = Snake()

game_is_on = True
while game_is_on:
	screen.update()  # Update the screen
	time.sleep(0.1)  # Pause to control the speed of the snake

	snake.move()

screen.exitonclick()
