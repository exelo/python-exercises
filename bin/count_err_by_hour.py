#!/usr/bin/python3

# Log file elb.log:Elastic Load Balancing
# Format: space delimited
# http yyyy-dd-mm-hour-mm-ss returning-error-code 4 5 6 7

# Don't fully remember the entire question/task but roughly like:
# Task: Obtain a count of all error code 500 by the hour ? 

from pprint import pprint

def read_file(logfile):
    with open(logfile, 'r') as fobj:
        lines = fobj.readlines()
        return lines

def main():
    err_code_500_lines = []

    # lets filter by only fields we need
    for line in read_file('elb.log'):
        split_line = line.split()
        timestamp = split_line[1]
        errorcode = split_line[2]

        # filter by the error code:500
        # after this point we can discard field 500 no need to save
        # would help to send to log with logger if need to debug
        if errorcode == "500":
            err_code_500_lines.append(timestamp)
    
    # for timestamp in err_code_500_lines: print(timestamp)

    # Idea, use a dictionary 
    # Key will be Date YYYY-MM-DD 
    # Value = Dictoinary Key=Hour and Value = counter by the hour
    # {YYYY-MM-DD: {HR: counter}
    
    dict_day_counter_by_hour = {}
    # split and parse for Date and hour 
    for timestamp in err_code_500_lines:
        split_timestamp = timestamp.split(":")
        year_month_day = split_timestamp[0]
        hour = split_timestamp[1]
        
        if year_month_day not in dict_day_counter_by_hour:
            dict_day_counter_by_hour[year_month_day] = {hour:1}
            continue

        if hour not in dict_day_counter_by_hour[year_month_day]:
            dict_day_counter_by_hour[year_month_day][hour] = 1 
            continue
        
        # we made it here we need to add 1 to the counter 
        dict_day_counter_by_hour[year_month_day][hour] += 1

    # lets pretty print our result
    pprint(dict_day_counter_by_hour)

if __name__ == "__main__":
    main()
