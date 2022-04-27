"""File: score.py

    Team No.: 02
    Author name: Matthew Dunlap
    Date completed: 04/27/2022
    
    Description: contains score class
"""
from main import *


if x == food.coordinates[0] and y == food.coordinates[1]:   #increase score, delete food with snake-food collision

    score
    score += 1
    label.config(text="Score{}".format(score))
    canvas.delete("food")
    food = Food()

else:       #we will only delete the last body part of our snake if we did not eat a food object.

    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
