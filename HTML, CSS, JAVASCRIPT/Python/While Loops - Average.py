''' 
While_loop_average.py -- Nguyen Hung Anh -- 09/20/2023
This program allows the user to input a series of numbers and returns
the average of the numbers

More specifically:
The function does not need any parameters.
The program should continue getting inputs until a negative number is entered.
The negative number should not be part of the average.
Assume that inputs are valid non-negative numbers.
'''

def get_keyboard_average():
    average = 0
    count_number = 0
    total_series_number = 0
    series_number = float(input("Your series number: "))
    while series_number >= 0:
        total_series_number += series_number
        count_number = count_number + 1
        series_number = float(input("Your series number: "))
    if count_number == 0:
        return float("nan")
    else:
        average = total_series_number / count_number
        return average
               
def main():
    f_average = get_keyboard_average()
    print("Your Average:", f_average)
if __name__ == "__main__":
    main()
