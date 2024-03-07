'''
Point_boxing.py - Nguyen Hung Anh - 09/11/2023
Given two points (x1y1) and (x2y2), representing opposing corners of a rectangle,
and a third point (x*y*) , determine if the third point is inside or on the edge of 
the rectangle defined by the other two points. These points may include decimals.
'''
def point_is_in_box(f_x1, f_y1, f_x2, f_y2, f_x, f_y):
    return (f_x1<=f_x<=f_x2 or f_x2<=f_x<=f_x1) and (f_y1<=f_y<=f_y2 or f_y2<=f_y<=f_y1)
def main():
    my_x1 = int(input("x1: "))
    my_y1 = int(input("y1: "))
    my_x2 = int(input("x2: "))
    my_y2 = int(input("y2: "))
    my_x = int(input("x: "))
    my_y = int(input("y: "))
    in_box=point_is_in_box(my_x1, my_x2, my_y1, my_y2, my_x, my_y)
    if in_box == True:
        print("In box")
    else:
        print("Not in box")
if __name__ == "__main__":
    main()
    
