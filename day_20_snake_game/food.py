import random

class FoodTime:
    def __init__(self):
        pass#self.starting_food = (0,0)
    
    def appear_position(self):
        x_pos = random.choice(range(-600, 601))
        y_pos = random.choice(range(-600, 601))
        position = self.starting_food.goto(x_pos, y_pos)
        return position