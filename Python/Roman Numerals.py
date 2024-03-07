'''
Roman_numerals.py -- Nguyen Hung Anh -- 09/13/2023
This program accepts a year written in base 10, as we would normally write
it, and outputs the equivalent year, written using Roman numerals.
'''

def year_to_roman(arabic_year):
    # Calculate the thousands place value and the remaining Arabic year
    th_arabic = arabic_year // 1000
    left_arabic = arabic_year % 1000

    # Calculate the hundreds place value and the remaining Arabic year
    one_h_arabic = left_arabic // 100
    left_arabic = left_arabic % 100

    # Calculate the tens place value and the remaining Arabic year
    ten_arabic = left_arabic // 10
    left_arabic = left_arabic % 10

    # The remaining Arabic year is the ones place value
    one_arabic = left_arabic

    # Convert thousands place value to Roman numeral
    s_th = th_arabic * "M"

    # Convert hundreds place value to Roman numeral
    if one_h_arabic == 9: 
        s_one_h = "CM"
    elif one_h_arabic >= 5:
        s_one_h = "D" + (one_h_arabic-5) * "C"
    elif one_h_arabic == 4:
        s_one_h = "CD"
    else:
        s_one_h = (one_h_arabic) * "C"

    # Convert tens place value to Roman numeral
    if ten_arabic == 9:
        s_ten = "XC"
    elif ten_arabic >= 5:
        s_ten = "L" + (ten_arabic-5) * "X"
    elif ten_arabic == 4:
        s_ten = "XL"
    else:
        s_ten = (ten_arabic) * "X"
        
    # Convert ones place value to Roman numeral
    if one_arabic == 9:
        s_one = "IX"
    elif one_arabic >= 5:
        s_one = "V" + (one_arabic-5) * "I"
    elif one_arabic == 4:
        s_one = "IV"
    else:
        s_one = (one_arabic) * "I"
        
    # Concatenate the Roman numerals for each place value
    s_roman_year = s_th + s_one_h + s_ten + s_one
    
    return s_roman_year

def main():
    # Take input from the user
    user_year = int(input("What year should be converted? "))

    # Convert the year to a Roman numeral
    s = year_to_roman(user_year)

    # Print the result
    print(user_year, "is", s)

if __name__ == "__main__":
    main()
    

