'''
Graphics_and_documentation.py (Part 2) -- Nguyen Hung Anh -- 11/14/2023

This module draws a bar chart using Zelle Graphics.
The program generates random bar heights, creates a nicely formatted chart,
and draws a red, rectangular "Exit" button at the center top of the window.
Clicking the button closes the window.

Functions:
draw_bar_chart(): Draws a bar chart with consistent spacing and random bar heights.
draw_exit_button(win): Draws a red, rectangular "Exit" button at the center top of the window.

Note: The module will run automatically, and the user only needs to click to close the window.
'''

from graphics import *
import random

def exit_button(win):

  # Define the width and height of the button
  button_w = 100
  button_h = 50
  get_width = win.getWidth()
  rectangular_button = Rectangle(Point((get_width - button_w)/2, button_h)
                                 , Point((get_width + button_w)/2, 0))
  rectangular_button.setFill("red") 

  # Display "Exit" text inside the button
  text_in_button = Text(Point(get_width/2, button_h/2), "Exit")
  rectangular_button.draw(win)
  text_in_button.draw(win)
  
  # Wait for a click event in the button area
  while True:
      click_point = win.getMouse()
      if (get_width - button_w)/2 < click_point.getX() < (
          get_width + button_w)/2 and 0 < click_point.getY() < button_h:
          
          # Close the window when the button is clicked
          win.close()
          break
        
# Function to draw a random number of bars with random heights
def drawbars(win, winH, winW, spaceBars):
  numberBars = random.randint(3,15)

  # Calculate the width of each bar
  barWidth = (winW - (numberBars + 1) * spaceBars) / numberBars
  print(barWidth)
  print(numberBars)
  
  # Loop to draw the bars
  for i in range(numberBars):
    randomHeight =  random.randint(25, 125)

    #RGB
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Define the coordinates of the current bar's rectangle
    firstPoint = Point((i + 1) * spaceBars + i * barWidth, winH - randomHeight)
    secondPoint = Point((i + 1) * spaceBars + (i+1) * barWidth, winH)
    currRectangle = Rectangle(firstPoint, secondPoint)

    # Random the colors for the rectangles
    currRectangle.setFill(color_rgb(r,g,b))
    currRectangle.draw(win)
  return  

def main():
  winH  = 400
  winW  = 800
  space = 50
  win = GraphWin("Draw Rectangle", winW, winH)
  win.setBackground("white")
  drawbars(win, winH, winW, space)
  exit_button(win)
if __name__ == "__main__":
  main()  
