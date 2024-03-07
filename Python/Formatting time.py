''' 
Formatting_Time.py -- Nguyen Hung Anh -- 09/06/2023
This program take an integer number of seconds as input. 
My program should assume that the input is a valid positive integer. 
The output should be a nicely-formatted time, 
with hours, minutes, and seconds, like this: hh:mm:ss.
'''

# Function to format seconds as time in the format hh:mm:ss
def format_seconds_as_time(second):
    # Calculate total minutes and total hours
    minute = second // 60
    hour = minute // 60
    
    # Calculate remaining minutes and seconds after subtracting hours
    minute_later = minute % 60
    second_later = second % 60
    
    # Format the time as hh:mm:ss
    format_seconds_time = (f"{hour:0>}") + ":" + (f"{minute_later:0>2}") + ":" + (f"{second_later:0>2}")
    
    return format_seconds_time

# Main function
def main():
    # Take input from the user
    my_second = int(input("How many seconds after midnight is it: "))
    
    # Format the seconds as time
    nicely_formatted_time = format_seconds_as_time(my_second)
    
    # Print the nicely formatted time
    print(f"{nicely_formatted_time}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()

