# Script: 08 - File Encryption (Part III)
# Author: Robert Gregor
# Date of latest revision: 26 APR 23

# Objectives
    # In Python, create a script that utilizes the cryptography library to:
        # Prompt the user to select a mode: 
            # Encrypt a file (mode 1)
            # Decrypt a file (mode 2)
            # Encrypt a message (mode 3)
            # Decrypt a message (mode 4)
            # If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
            # If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
        # Depending on the selection, perform one of the below functions. You’ll need to create four functions:
            # Encrypt the target file if in mode 1
                # Delete the existing target file and replace it entirely with the encrypted version
            # Decrypt the target file if in mode 2
                # Delete the encrypted target file and replace it entirely with the decrypted version
            # Encrypt the string if in mode 3
                # Print the ciphertext to the screen
            # Decrypt the string if in mode 4
                # Print the cleartext to the screen

    # PART II Objectives - Protecting Data at Rest
        # Add a feature capability to your script to:
            # Recursively encrypt a single folder and all its contents
            # Recursively decrypt a single folder that was encrypted by this tool

    # PART III Objectives - Ransomware
        # Add a feature capability to your script to:
            # Alter the desktop wallpaper on a Windows PC with a ransomware message
            # Create a popup window on a Windows PC with a ransomware message
            # Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.
            # Add additional features that draw the computer user’s attention to the ransomware message.

# Stretch Goals (Optional Objectives):
    # Prompt the user if the output file should be compressed to an archive
    # If user responds ‘y’ for yes, compress resulting file to an archive
        # Refer to How to Compress and Decompress Files in Python or use os library to perform OS-specific archival commands

# Code Fellows Sources
    # [cryptography 40.0.2](https://pypi.org/project/cryptography/)
    # [How to Encrypt and Decrypt Files in Python](https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python)
    # [Python: List Of Files In Directory And Subdirectories](https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/)
    # [Recursive File and Directory Manipulation in Python](https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/)

# My Sources
    # [How to Clear Screen in Python?](https://www.scaler.com/topics/how-to-clear-screen-in-python/)
    # [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
    # [Compressing and Extracting Files in Python](https://code.tutsplus.com/tutorials/compressing-and-extracting-files-in-python--cms-26816)
    # [Context Managers and Python's with Statement](https://realpython.com/python-with-statement/)
    # [zipfile — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
    # [Python's zipfile: Manipulate Your ZIP Files Efficiently](https://realpython.com/python-zipfile/)
    # [Python | os.path.join() method](https://www.geeksforgeeks.org/python-os-path-join-method/)
    # [os.path — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
    # [Python os.walk() Method](https://www.tutorialspoint.com/python/os_walk.htm)
    # [os.path — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)

#!/usr/bin/env python3

# Import libraries
import os
import zipfile
from cryptography.fernet import Fernet
import ctypes
import tempfile
import urllib.request
import time

def write_key():
    # Generate key and store in key variable
    key = Fernet.generate_key()
    # Open / create key.key file, write as binary, refer to key.key as key_file
    with open("key.key", "wb") as key_file:
        # Write contents of key variable to key.key file
        key_file.write(key)

def load_key():
    # Load and return key from current key.key file
    return open("key.key", "rb").read()

def compress_file(encrypt_file):
    # With statement used to create context, zipfile.Zipfile function executed to write encrypt_file as compressed_file
    with zipfile.ZipFile(encrypt_file, 'w') as compressed_file:
        # Write method called on compressed_file to add file to archive, ZIP_DEFLATED algorithm used to compress
        compressed_file.write(encrypt_file, compress_type=zipfile.ZIP_DEFLATED)
        # Print comformation of compression
        print(f"\nYou have successfully compressed and archived {encrypt_file}")

def encrypt_file(file_path):
    # Load encryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)    
 
    # Read file content as binary
    with open(file_path, "rb") as file:
        file_data = file.read()        
    # Encrypt file content
    encrypted_file = f.encrypt(file_data)    
    # Write encrypted content to file
    with open(file_path, "wb") as file:
        file.write(encrypted_file)

def decrypt_file(file_path):
    # Load decryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)    

    # Read file content as binary
    with open(file_path, "rb") as file:
        encrypted_data = file.read()        
    # Decrypt file content
    decrypted_data = f.decrypt(encrypted_data)    
    # Write decrypted content to file
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_string():
    # Load encryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)
    # Get the message string to encrypt from user
    message = input("\nEnter message to encrypt: ")
    # Encrypt the message string
    encrypted_message = f.encrypt(message.encode())
    # Print the encrypted message string
    print("\nEncrypted message: ", encrypted_message.decode())

def decrypt_string():
    # Load decryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)
    # Get the encrypted message string to decrypt from user
    encrypted_string = input("\nEnter encrypted string to decrypt message: ")
    # Decrypt the encrypted message string
    decrypted_string = f.decrypt(encrypted_string.encode())
    # Print the decrypted message string
    print("\nDecrypted message: ", decrypted_string.decode())

def encrypt_folder():
    # Load the key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)
    # Accept user input and assign folder_path variable
    folder_path = input("\nEnter path to folder to encrypt: ")
    # For loop iterates through all dirs & files in folder_path
    for root, dirs, files in os.walk(folder_path):
        # Iterate through each file provided by os.walk function
        for file in files:
            # Concatanate root dir and file to create file_path
            file_path = os.path.join(root, file)
            # Execute encrypt_file function with file_path arguement
            encrypt_file(file_path)
    # Print success to screen
    print(f"\nYou have successfully encrpyted the {folder_path} folder!")

def decrypt_folder():
    # Load the key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)
    # Accept user input and assign folder_path variable
    folder_path = input("\nEnter path to folder to decrypt: ")
    # For loop iterates through all dirs & files in folder_path
    for root, dirs, files in os.walk(folder_path):
        # Iterate through each file provided by os.walk function
        for file in files:
            # Concatanate root dir and file to create file_path
            file_path = os.path.join(root, file)
            # Execute decrypt_file function with file_path arguement
            decrypt_file(file_path)
    # Print success to screen
    print(f"\nYou have successfully decrpyted the {folder_path} folder!")

def ransom_sim():
    # Set background image URL
    background_image = "https://wallpapercave.com/wp/wp9680895.jpgg"
    # Path variable sets image save location
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'background.jpg')
    # Download image and save to path
    urllib.request.urlretrieve(background_image, path)
    # Set download image as desktop background
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    # Pause 2 seconds
    time.sleep(2)
    # Display 10 pop-up's
    for _ in range(10):
        ctypes.windll.user32.MessageBoxW(0, "YOU'VE BEEN INFECTED WITH RANSOMWARE!!!", "Message", 0x40 | 0x1)

# Execute write_key() function
write_key()

# Execute load_key() function
load_key()

# Clear terminal screen
os.system('clear')

while True:
      
        print("\n------------------------")
        print("Please choose an option:")
        print("------------------------")
        print("1) Encrypt file\n2) Decrypt file\n3) Encrypt message string\n4) Decrypt message string\n5) Encrypt folder\n6) Decrypt folder\n7) Ransom Simulation\nexit) exit program")
        user_option = str(input("------------------------\n"))

        if user_option == "1":
            file_path = input("Enter path to filename to encrypt: ")
            encrypt_file(file_path)
        elif user_option == "2":
            file_path = input("Enter path to filename to decrypt: ")
            decrypt_file(file_path)
        elif user_option == "3":
            encrypt_string()
        elif user_option == "4":
            decrypt_string()
        elif user_option == "5":
            encrypt_folder()
        elif user_option == "6":
            decrypt_folder()
        elif user_option == "7":
            ransom_sim()
        elif user_option == "exit":
            print("\nExited successfully!\n")
            exit()
        else:
            print("\nInvalid input please try again!")
            continue

# End