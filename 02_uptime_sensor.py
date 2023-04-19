# Script: 02 - Uptime Sensor Tool (Part 1)
# Author: Robert Gregor
# Date of latest revision: 18 APR 23

# Objectives
    # In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down
        # Transmit a single ICMP (ping) packet to a specific IP every two seconds
        # Evaluate the response as either success or failure
        # Assign success or failure to a status variable
        # For every ICMP transmission attempted, print status variable along with comprehensive timestamp and destination IP tested
            # Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

# Stretch Goals (Optional Objectives)
    # In Python, add the below features to your uptime sensor tool
        # Save the output to a text file as a log of events
        # Accept user input for target IP address

# Code Fellows Sources
    # [How to print current date and time using Python?](https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python)
    # [Python time sleep() Method](https://www.tutorialspoint.com/python/time_sleep.htm)
    # [Python while Loop Statements](https://www.tutorialspoint.com/python/python_while_loop.htm)
    # [Python Ping: How to ping with Python](https://www.ictshore.com/python/python-ping-tutorial/)
    # [Ping 0.2: An implementation of ICMP ping in Python](https://pypi.org/project/ping/)

# My Sources
    # [Python Looping Through a Range](https://www.w3schools.com/python/gloss_python_for_range.asp)
    # [Python append to a file](https://www.geeksforgeeks.org/python-append-to-a-file/)

#!/usr/bin/env python3

# Main

import datetime
import click
import time
from pythonping import ping

def ping_userIP(user_IP):

    # Declares ping_log variable equal to string
    ping_log = "ping_log.txt"

    # While loop used to ping user supplied IP
    while True:

        # Declares ping_result variable equal to output of ping command
        ping_result = ping(user_IP, count=1, timeout=1)

        # Determines ping_status variable content case on ping_result.success() function return value
        if ping_result.success():
            ping_status = "Network ACTIVE to host"
        else:
            ping_status = "Network INACTIVE to host"

        # Declares current_time variable equal to time now and formats output
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Stores current_time, ping_status, and user-IP variables as string in ping_entry variable and prints output to screen
        ping_entry = f"{current_time} - {ping_status} {user_IP}"
        print(ping_entry)

        # Creates ping_log file, opens it in append mode, and writes/appends ping_entry variable contents to file
        with open(ping_log, "a") as file:
            file.write(ping_entry + "\n")

        # Provides two second delay between ping commands
        time.sleep(2)

while True:
    click.clear()
    print("-------------------------------------")
    print("Welcome to the uptime sensor program!")
    print("-------------------------------------\n")
 
    # Requests user_IP input and converts to string
    user_IP = str(input("Please enter the IP address you would like to ping (or type 'exit'): "))
    print()

    # Conditional supporting exit functionality
    if user_IP == "exit":
        print("You have exited the uptime sensor program successfully!\n")
        exit()

    # Call the ping_userIP function with the user_IP variable as an arguement
    ping_userIP(user_IP)

    # Enter to return to IP input
    input("\nPress Enter to continue...")

# End