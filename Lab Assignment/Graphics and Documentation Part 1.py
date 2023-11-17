'''
Graphics_and_Documentation.py (Part 1) -- Nguyen Hung Anh -- 11/03/2023

This module allows the user to draw a triangle using Zelle Graphics.
The program marks the corners as the user clicks three times, highlights the triangle,
computes its area, and displays the area on the graphics window.
Additionally, a red, rectangular "Exit" button is drawn at the center top of the window,
and clicking the button closes the window.

* Functions:
draw_triangle(): Allows the user to draw a triangle, computes its area, and displays the result.
draw_exit_button(win): Draws a red, rectangular "Exit" button at the center top of the window.
Note: The user needs to click three times to draw the triangle.
'''

from graphics import *
    
def draw_triangle(win):

    user_points = []

    # Allow the user to click three points to define the vertices of the triangle
    for i in range(3):
        click_point = win.getMouse()
        user_points.append(click_point)
        
        # Display a red circle at each clicked point
        points_circle = Circle(click_point, 2)
        points_circle.setFill("red")
        points_circle.draw(win)
        
    # Create a polygon connecting the user-defined points to form the triangle    
    connect_points = Polygon(user_points)
    connect_points.setWidth(1)
    connect_points.draw(win)
    connect_points.setFill("yellow")


    return user_points

def triangle_area(user_points):
    
    # Extract the coordinates of the three vertices of the triangle
    x1 = user_points[0].getX()
    x2 = user_points[1].getX()
    x3 = user_points[2].getX()
    y1 = user_points[0].getY()
    y2 = user_points[1].getY()
    y3 = user_points[2].getY()

    # Calculate the area of the triangle using the determinant formula
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    return area

def exit_button(win):
    # Create an "Exit" button as a rectangular shape
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
    
    while True:
        click_point = win.getMouse()
        if (get_width - button_w)/2 < click_point.getX() < (
            get_width + button_w)/2 and 0 < click_point.getY() < button_h:
            
            # Close the window when the button is clicked
            win.close()
            break

def main():
    win_height = 400
    win_widht = 400
    
    # Create a graphical window
    win = GraphWin("Draw Triangle", win_widht, win_height)
    win.setBackground("white")
    triangle = draw_triangle(win)
    area = triangle_area(triangle)
    area_text = Text(Point(win_widht * 0.8, win_height * 0.8), f"Area: {area}")
    area_text.setSize(12)
    area_text.draw(win)
    exit_button(win)

if __name__ == "__main__":
    main()
    

