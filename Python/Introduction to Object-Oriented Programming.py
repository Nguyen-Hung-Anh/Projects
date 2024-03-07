'''
Introduction_to_object_oriented_programming.py -- Nguyen Hung Anh -- 11/17/2023
'''

import math

class Complex:
    def __init__(self, real, imag):
        # Constructor to initialize the real and imaginary parts of the complex number
        self.real = real
        self.imag = imag

    def __str__(self):
        # String conversion method for a user-friendly representation of the complex number
        return f'{self.real}+{self.imag}i'

    def __repr__(self):
        # Object representation for debugging and development purposes
        return f'Complex({self.real}, {self.imag})'

    def add(self, other):
        # Method for adding two complex numbers
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return Complex(real_sum, imag_sum)

    def sub(self, other):
        # Method for subtracting one complex number from another
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return Complex(real_diff, imag_diff)

    def mult(self, other):
        # Method for multiplying two complex numbers
        real_mult = self.real * other.real - self.imag * other.imag
        imag_mult = self.real * other.imag + self.imag * other.real
        return Complex(real_mult, imag_mult)

    def modulus(self):
        # Method for calculating the modulus (magnitude) of the complex number
        return math.sqrt(self.real ** 2 + self.imag ** 2)

def main():
    # Testing the Complex class with two instances
    a = Complex(1, 2)
    b = Complex(2, 3)

    # Displaying the complex numbers
    print(a)
    print(b)

    # Displaying the modulus of the complex numbers
    print(f'|{a}| = {a.modulus()}')
    print(f'|{b}| = {b.modulus()}')

    # Displaying the result of addition and multiplication of the complex numbers
    print(f'{a} + {b} = {a.add(b)}')
    print(f'{a} * {b} = {a.mult(b)}')

if __name__ == '__main__':
    main()
