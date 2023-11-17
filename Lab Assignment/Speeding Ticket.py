'''
Speeding Ticket.py -- CSC 170b F'23 Collective authorship - Nguyen Hung Anh
'''
def did_get_ticket(b_your_birthday, f_your_speed):
    if b_your_birthday:
        f_your_speed = f_your_speed - 5
    if f_your_speed < 60: # no b-day, no fine
        print("No fine")
    elif f_your_speed <= 80:
        print("Small fine")
    else:
        print("Big fine")

    
def main():
    f_your_speed = float(input"Your Speed: ")
    b_your_birthday = "y" == intput("Birthday: (y/n)")
    did_get_ticket(b_your_birthday, f_your_speed)
    
##    if b_your_birthday and f_your_speed < 65:
##        print("No fine")
##    elif b_your_birthday and 65 <= f_your_speed <= 85:
##        print("Small fine")
##    else b_your_birthday and f_your_speed > 85:
##        print("Big fine")
##    elif f_your_speed < 60: # no b-day, no fine
##        print("No fine")
##    elif f_your_speed 60<= f_your_speed <= 80:
##        print("Small fine")
##    elif f_your_speed > 80:
##        print("Big fine")

if __name__=="__main__":
    main()
