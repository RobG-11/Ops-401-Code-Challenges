# Script: 02 - Uptime Sensor Tool
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

# My Sources:
    # []()
    

#!/usr/bin/env python3

# Main

import os, datetime, click

while True:
    click.clear()
    print("-------------------------------------")
    print("Welcome to the uptime sensor program!")
    print("-------------------------------------\n")
 
    # Requests user_IP input and converts to string
    user_IP = str(input("Please enter the IP address you would like to ping (or type 'exit'): "))

    if user_IP == "exit":
        print("\nYou have exited the uptime sensor program successfully!\n")
        exit()

# End