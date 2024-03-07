'''
While_loops_square_roots -- Nguyen Hung Anh - 09/20/2023
This programfind the square root of a number A using Newton's method
'''
def square_root(a):
    x0 = (a / 2)
    distand = 10 ** -8
    while True:
        xn = x0 - (x0 ** 2 - a) / (2 * x0)
        if abs(xn - x0) < distand:
            return xn
        x0 = xn
        
def main():
    a = float(input("Enter a number to find its square root: "))
    result = square_root(a)
    print(f"Your Square Root is {result:.8f}")
                           
if __name__=="__main__":
    main()
