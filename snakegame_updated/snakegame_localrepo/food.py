"""File: food.py

    Team No.: 02
    Author name: Matthew Dunlap
    Date completed: 04/27/2022
    
    Description: contains food class
"""
from main import *


class Food:
    
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")