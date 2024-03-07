'''
Temperature Conversion.py -- Robert Nguyen/Nguyen Anh -- 09/04/2023
This program converts a temperature in Fahrenheit to Celius.
'''
def fahrenheit_to_celsius(fahrenheit_value):
    celsius = 5/9 * (float(fahrenheit_value) - 32)
    return celsius
def main():
    my_fahrenheit = float(input("Temperature in Fahrenheit: "))
    my_celsius = fahrenheit_to_celsius(my_fahrenheit)
    print(f"Temperature in C:{my_celsius:.>20.15f}\N{DEGREE SIGN}C")

if __name__ =="__main__":
    main()

