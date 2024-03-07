''' 
Ride_at_your_Own_Risk -- Nguyen Hung Anh -- 09/08/2023
 This program defines a fairground ride policy with the can_ride() function.
 The function takes has_waiver (bool), height (int), and age (int).
 Policy: Taller than 120cm or 12 years and older, with a waiver, can ride.
 Returns boolean. Main() calls can_ride() and prints the result in one statement.
 Assumes valid inputs.
'''
              
def main():
    i_your_age = int(input("Age (yrs): "))       
    f_your_height = float(input("Height (cm): "))
    i_sign = input("Waiver signed (y/n)?: ").lower()
    result = (i_your_age > 12 or f_your_height > 120.0) and i_sign == 'y'
    if result == True:
        print("Yes you can play")
    else:
        print("Sorry! you can't play")
if __name__ == "__main__":
    main()
