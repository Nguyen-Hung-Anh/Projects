'''
Refactoring_functions.py -- Nguyen Hung Anh -- 11/08/2023

This program calculates the area of a triangle using Heron's formula.
It takes user input for the lengths of the triangle sides, checks if
the sides form a valid triangle, calculates the area, and displays
the information.
'''
import math

def get_point(counter):
    x = float(input(f"Point {counter} x : "))
    y = float(input(f"Point {counter} y : "))
    return x, y

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_semi_perimeter(a, b, c):
    return (a + b + c) / 2

def calculate_area(a, b, c, s):
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
def main():
    # Get the points:
    x1, y1 = get_point(1)
    x2, y2 = get_point(2)
    x3, y3 = get_point(3)

    # Calculate side lengths
    a = calculate_distance(x1, y1, x2, y2)
    b = calculate_distance(x2, y2, x3, y3)
    c = calculate_distance(x3, y3, x1, y1)

    # Calculate semi-perimeter
    s = calculate_semi_perimeter(a, b, c)

    # Calculate and print the area
    area = calculate_area(a, b, c, s)

    print("The area defined by the points:")
    print(f"({x1}, {y1})")
    print(f"({x2}, {y2})")
    print(f"({x3}, {y3})", end="\n\n")
    print("is", area)

if __name__ == "__main__":
    main()


