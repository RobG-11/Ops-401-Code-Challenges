# Script: 36 - Web Application Fingerprinting **COMPLETE**
# Author: Robert Gregor
# Date of latest revision: 06 JUN 23

# Objectives - Create a script that executes from a Linux box to perform the following:
    # Prompts the user to type a URL or IP address and a port number
    # Performs banner grabbing using netcat against target address at target port
        # Prints results to screen then moves on to step below
    # Performs banner grabbing using telnet against target address at target port
        # Prints results to screen then moves on to step below
    # Performs banner grabbing using Nmap against the target address of all well-known ports
        # Prints the results to the screen

# My Sources
    # [Multiple Ways to Banner Grabbing](https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/)
    # [Python Lists](https://www.geeksforgeeks.org/python-lists/)
    # [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html)
    # [How to use subprocess popen Python](https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python)
    # [Understanding Popen.communicate](https://stackoverflow.com/questions/16768290/understanding-popen-communicate)
    # [An Introduction to Subprocess in Python With Examples](https://www.simplilearn.com/tutorials/python-tutorial/subprocess-in-python)

#!/usr/bin/env python

# Import modules
import subprocess, time, os

def netcat_bgrab(user_url, user_port):
    print(f"\nPerforming banner grabbing with netcat against {user_url} port {user_port}...\n")
    time.sleep(2)
    # Create list of items required to run command
    command = ["nc", "-v", "-n", "-w2", user_url, user_port]
    # Execute command with subprocess.Popen, pipes stdout and stderr to variables
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Captures stdout and stderr
    output, error = process.communicate()
    # Conditional determines if any output is provided
    if output:
        # Data decoded to string, whitespace stripped, and then printed to terminal
        print(output.decode().strip())
    else:
        print("No banner information found")

def telnet_bgrab(user_url, user_port):
    print(f"\nPerforming banner grabbing with telnet against {user_url} port {user_port}...\n")
    time.sleep(2)
    # Create list of items required to run command
    command = ["telnet", user_url, user_port]
    # Execute command with subprocess.Popen, pipes stdout and stderr to variables
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Captures stdout and stderr
    output, error = process.communicate()
    # Conditional determines if any output is provided
    if output:
        # Data decoded to string, whitespace stripped, and then printed to terminal
        print(output.decode().strip())
    else:
        print("No banner information found")

def nmap_bgrab(user_url):
    print(f"\nPerforming banner grabbing with nmap against {user_url} commonly known ports (1-1023)...\n")
    time.sleep(2)
    # Create list of items required to run command
    command = ["nmap", "-p1-1023", "-sV", "--version-intensity", "0", user_url]
    # Execute command with subprocess.Popen, pipes stdout and stderr to variables
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Captures stdout and stderr
    output, error = process.communicate()
    # Conditional determines if any output is provided
    if output:
        # Data decoded to string, whitespace stripped, and then printed to terminal
        print(output.decode().strip())
    else:
        print("No banner information found")

# Clear terminal
os.system('clear')

# Request user input
user_url = input(str("Enter the URL where you would like to conduct banner grabbing (ex. scanme.nmap.org):\n\n"))
user_port = input(str("\nEnter the port where you would like to conduct banner grabbing (ex. 443):\n\n"))

# Execute functions (2 sec delay) with parameters
netcat_bgrab(user_url, user_port)
time.sleep(2)
telnet_bgrab(user_url, user_port)
time.sleep(2)
nmap_bgrab(user_url)
