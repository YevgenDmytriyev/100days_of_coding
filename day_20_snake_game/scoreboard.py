from snake import *
from food import *

snake = Snake()
food = FoodTime()

class Scoreboard:
    def __init__(self,match_position):
        self.match_position = match_position
        
    def score_count(self):
        score = 0
        if snake.head.position() == food.appear_position():
            score += 1
        