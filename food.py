"""File: window_and_canvas.py
Team No.: 2
Author name: Loftus
Date completed: 04/19/22
Description: food class for randomizing food in game.
"""

from window_and_canvas import *
from tkinter import *
import random
from tkinter import font

playground_width = 500
playground_height = 500
block_size = 20
food_color = '#63ace5'

class Food:
    def __init__(self):
        
        x = random.randint(0, (playground_width / block_size) - 1) * block_size 
        #random generates food on x coord.; can only appear on one of the blocks on canvas, -1 to be exclusive
        y = random.randint(0, (playground_height / block_size) - 1) * block_size
        #same for above, just for y coord
        self.coordinates = [x,y] #setting the coordinates

        canvas.create_oval(x, y, x + block_size, y + block_size, fill = food_color)
        #This is the actual shape of the food, and the coord. it can randomize in

