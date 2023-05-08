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

# My Sources:
    # [With Open in Python – With Statement Syntax Example](https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/)
    # []()
    # []()
    # []()

#!/usr/bin/env python

# Import libraries
import time, getpass, os

def wordlist_iterate():
    # Accepts user input path to wordlist
    word_list = str(input("\nPlease enter the path to your word list (ex. /home/user/wordlist.txt)):\n"))
    # With statement opens word_list file in read mode as file
    with open(word_list, 'r') as file:
        # For loop iterates through each line in word_list
        for line in file:
            # Rmoves leading and trailing white space, breaks line into list of words
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
                
def recog_passwd():
    word_list = str(input("\nPlease enter the path to your word list (ex. /home/user/wordlist.txt)):\n"))
    user_passwd = str(input("\nPlease enter the password you would like to query:\n"))

    if os.path.isfile(word_list):
        with open(word_list, 'r') as file:
            for line in file:
                passwords = line.strip().split()
                if user_passwd in passwords:
                    print(f"\nPassword '{user_passwd}' was found in the {word_list} word list")
                    break
            else:
                print(f"\nPassword '{user_passwd}' was not found in the {word_list} word list")

def complex_passwd():
    exit()

while True:
      
        print("\n------------------------")
        print("Please choose an option:")
        print("------------------------")
        print("1) List all passwords in word list\n2) Password in word list?\n3) Password complexity evaluation\nexit) Exits program")
        user_option = str(input("------------------------\n"))

        if user_option == "1":
            wordlist_iterate()
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

