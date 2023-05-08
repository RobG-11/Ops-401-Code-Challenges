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
    # [Python | os.path.isfile() method](https://www.geeksforgeeks.org/python-os-path-isfile-method/)
    # [os.path — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
    # [re.findall()](https://www.codecademy.com/resources/docs/python/regex/findall)
    # [Python Regex: re.search() VS re.findall()](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
    # 

#!/usr/bin/env python

# Import libraries
import time, getpass, os, re

def wordlist_iterate():
    # Accepts user input path to wordlist
    word_list = str(input("\nPlease enter the path to your word list (ex. /home/user/wordlist.txt)):\n"))
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
        print("Password length requirement: Satisfied")
    else:
        print(f"Password length requirement: Not satisfied (minimum {min_length} characters)")

    # re.findall function counts how many capital letters are found in user_passwd
    capital_letters = re.findall(r'[A-Z]', user_passwd)
    # Conditional used to determine if number of capital letters used meets requirements
    if len(capital_letters) >= min_capital_letters:
        print("Capital letter requirement: Satisfied")
    else:
        print(f"Capital letter requirement: Not satisfied (minimum {min_capital_letters} capital letters)")

    # re.findall function counts how many numbers are found in user_passwd
    numbers = re.findall(r'\d', user_passwd)
    # Conditional used to determine if number of numbers used meets requirements
    if len(numbers) >= min_numbers:
        print("Number requirement: Satisfied")
    else:
        print(f"Number requirement: Not satisfied (minimum {min_numbers} numbers)")

    # re.findall function counts how many specified special characters are found in user_passwd
    special_characters = re.findall(r'[!@#$%^&*(),.?":{}|<>]', user_passwd)
    # Conditional used to determine if number of special characters used meets requirements
    if len(special_characters) >= min_special_characters:
        print("Special character requirement: Satisfied")
    else:
        print(f"Special character requirement: Not satisfied (minimum {min_special_characters} special characters)")

    # Conditional determines if all requirements are met using boolean logic
    if (len(user_passwd) >= min_length and
        len(capital_letters) >= min_capital_letters and
        len(numbers) >= min_numbers and
        len(special_characters) >= min_special_characters):
        print("\nSUCCESS! YOU HAVE MET PASSWORD COMPLEXITY REQUIREMENTS!")

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

