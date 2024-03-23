from turtle import Turtle, Screen
from snake import Snake
from food import FoodTime

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create instances of Snake and Food
snake = Snake()
food = FoodTime()

# Listen for key events to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    # Check if snake collides with food
    if snake.head.distance(food.position()) < 15:
        food.refresh()
        snake.extend()
    
    # Check if snake collides with wall
    if (
        abs(snake.head.xcor()) > 290
        or abs(snake.head.ycor()) > 290
        or snake.head.distance(snake.segments[1]) < 10
    ):
        game_is_on = False

# End of game
screen.exitonclick()

