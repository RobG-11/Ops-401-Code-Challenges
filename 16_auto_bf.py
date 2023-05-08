# Script: 16 - Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author: Robert Gregor
# Date of latest revision: 08 MAY 23

# Objectives (PART I)
    # In Python, create a script that prompts the user to select one of the following modes:
        # Mode 1: Offensive; Dictionary Iterator
            # Accepts user input word list file path
                # Iterates through the word list, assigning the word being read to a variable.
            # Add a delay between words.
            # Print to the screen the value of the variable
        # Mode 2: Defensive; Password Recognized
            # Accepts a user input string.
            # Accepts a user input word list file path.
            # Search the word list for the user input string.
            # Print to the screen whether the string appeared in the word list.
        # Mode 3: Defensive; Password Complexity (STRETCH GOAL)
            # Accepts a user input string.
                # Evaluates the user input string for password complexity
            # Impose a requirement in your code for the below metrics:
                # Were at least [qty] characters used (password length)?
                # Were at least [qty] capital letter used?
                # Were at least [qty] numbers used?
                # Were at least [qty] symbols used?
            # Prints to the screen which of the above dimensions were satisfied by the user input password. 
                # If all dimensions are satisfied, print a clear SUCCESS indicator for the user.

# Code Fellows Sources:
    # [Iterate over a set in Python](https://www.geeksforgeeks.org/iterate-over-a-set-in-python/)
    # [RockYou Password List](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)

#!/usr/bin/env python

# Import libraries
import time, getpass

def dict_iterate():
    exit()

def recog_passwd():
    exit()

def complex_passwd():
    exit()

while True:
      
        print("\n------------------------")
        print("Please choose an option:")
        print("------------------------")
        print("1) Encrypt file\n2) Decrypt file\n3) Encrypt message string\nexit) Exits program")
        user_option = str(input("------------------------\n"))

        if user_option == "1":
            dict_iterate()
        elif user_option == "2":
            recog_passwd()
        elif user_option == "3":
            complex_passwd()
        elif user_option == "exit":
            print("\nExited successfully!\n")
            exit()
        else:
            print("\nInvalid input please try again!")
            continue

