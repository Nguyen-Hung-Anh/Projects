''' 
Formatting_Time.py -- Nguyen Hung Anh -- 09/06/2023
This program take an integer number of seconds as input. 
My program should assume that the input is a valid positive integer. 
The output should be a nicely-formatted time, 
with hours, minutes, and seconds, like this: hh:mm:ss.
'''

def format_seconds_as_time(second):
    minute = second // 60
    hour = minute // 60
    minute_later = minute % 60
    second_later = second % 60
    format_seconds_time = (f"{hour:0>}")+ ":" +(f"{minute_later:0>2}")+ ":" +(f"{second_later:0>2}")
    return format_seconds_time

def main():
    my_second = int(input("How many seconds after midnight is it: "))
    nicely_formatted_time = format_seconds_as_time(my_second)
    print(f"{nicely_formatted_time}")

if __name__=="__main__":
    main()

