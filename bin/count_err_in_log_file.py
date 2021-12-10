#!/usr/bin/python3

# Elastic Load Balancing log file
# Format: space delimited
# <app> <timestamp> <sendr> <webserver> <error return code> <code> <7th> <8th> <9th> <10th> <11th>
# Task
# Obtain a count of all error return code 500 per hour from the log 

from pprint import pprint

def read_file(logfile):
    with open(logfile, 'r') as fobj:
        lines = fobj.readlines()
        return lines

def main():
    err_code_500_lines = []
    log_file_name = "logs/web-server.log"
    # filter by only fields we need
    # timestamp and error return code
    for line in read_file(log_file_name):
        split_line = line.split()
        # print(f"split_line:{split_line}")
        timestamp = split_line[1]
        errorcode = split_line[4]

        # filter by the error return code:500
        # after this point we can discard field 500
        # helpful to send to a log if need to debug
        if errorcode == "500":
            err_code_500_lines.append(timestamp)
    
    # for timestamp in err_code_500_lines: print(timestamp)

    # Idea, use a Dictionary 
    # Key: YYYY-MM-DD (Date) 
    # Value = Dictoinary={Key=Hour: Value=counter(per hour)}
    # {YYYY-MM-DD: {Hour: Counter}
    
    dict_counter_per_hour = {}
    # split and parse for Date and hour  
    for timestamp in err_code_500_lines:
        split_timestamp = timestamp.split(":")
        year_month_day = split_timestamp[0]
        hour = split_timestamp[1]
        
        if year_month_day not in dict_counter_per_hour:
            dict_counter_per_hour[year_month_day] = {hour:1}
            continue

        if hour not in dict_counter_per_hour[year_month_day]:
            dict_counter_per_hour[year_month_day][hour] = 1 
            continue
        
        # Add 1 to the counter 
        dict_counter_per_hour[year_month_day][hour] += 1
    
    # pretty print
    pprint(dict_counter_per_hour)

if __name__ == "__main__":
    main()
