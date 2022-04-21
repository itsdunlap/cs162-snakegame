"""File: window_and_canvas.py
Team No.: 2
Author name: Loftus
Date completed: 04/19/22
Description: This is the window and canvas for the game to be played in.
TUTORIAL HELP: https://www.youtube.com/watch?v=hDOGYnqv2jw """

from tkinter import *
import random
from tkinter import font

playground_width = 500
playground_height = 500
snake_color = '#2a4d69' 
bkg_color = '#adcbe3'
food_color = '#63ace5'
""" all of this is changable, adjustable. can use
again in other tkinter games."""

window = Tk()
window.title("The Hungry Snake Man") #title of game
window.resizable(300, 300) #change the window size here

global score #if we don't need this, we can take it out
score = 0

label = Label(window, text="your score: {}".format(score), font=('Helvetica', 20))
label.pack() #A label for the scoreboard element

canvas = Canvas(window, background=bkg_color, height=playground_height, width=playground_width)
canvas.pack()

