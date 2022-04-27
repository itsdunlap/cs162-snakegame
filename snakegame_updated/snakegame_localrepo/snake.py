"""File: snake.py

    Team No.: 02
    Author name: Matthew Dunlap
    Date completed: 04/27/2022
    
    Description: contains Snake class
"""
#from tkinter import *
import main


class Snake:

    def __init__(self):
        self.body_size = main.BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, main.BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = main.canvas.create_rectangle(x, y, x + main.SPACE_SIZE, y + main.SPACE_SIZE, fill=main.SNAKE_COLOR, tag="snake")
            self.squares.append(square)