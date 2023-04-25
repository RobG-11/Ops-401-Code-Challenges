# Script: 07 - File Encryption (Part II)
# Author: Robert Gregor
# Date of latest revision: 25 APR 23

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

#!/usr/bin/env python3

# Import libraries
import os
import zipfile
import io
from cryptography.fernet import Fernet

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

def encrypt_file():
    # Load encryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)    
    # Get filename to encrypt
    encrypt_file = input("Enter path to filename to encrypt: ")    
    # Read file content as binary
    with open(encrypt_file, "rb") as file:
        file_data = file.read()        
    # Encrypt file content
    encrypted_file = f.encrypt(file_data)    
    # Write encrypted content to file
    with open(encrypt_file, "wb") as file:
        file.write(encrypted_file)

    # Request if user would like to compress output file to an archive
    archive_file = input(f"\nWould you like to compress {encrypt_file} to an archive (Y/N)?: ")

    # Conditional determines if user would like compression, if so compress_file() funtion is executed with selected file as arguement
    if archive_file == "Y":
        compress_file(encrypt_file)
    elif archive_file == "N":
        pass
    else:
        print("\nInvalid input please try again!")
        
def decrypt_file():
    # Load decryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)    
    # Get filename to decrypt
    decrypt_file = input("Enter path to filename to decrypt: ")    
    # Read file content as binary
    with open(decrypt_file, "rb") as file:
        encrypted_data = file.read()        
    # Decrypt file content
    decrypted_data = f.decrypt(encrypted_data)    
    # Write decrypted content to file
    with open(decrypt_file, "wb") as file:
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
    # Load decryption key
    key = load_key()
    # Create Fernet object with loaded key
    f = Fernet(key)
    # Get folder path to encrypt
    folder_path = input("\nEnter path to folder to encrypt: ")
    
    # Compress Folder - Strips path from folder_path and set folder_name equal to target folder
    folder_name = os.path.basename(folder_path)
    # Appends .zip to folder_name
    compressed_folder_path = folder_name + '.zip'
    # Creates new zip file with ZIP_DEFLATED compression method and the highest compression level (9)
    with zipfile.ZipFile(compressed_folder_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        # Iterates over all items in folder_path with os.walk() function
        for root, _, files in os.walk(folder_path):
            # Iterates over all files in files list
            for file in files:
                # Creates full file path by joining root and file with os.path.join() function
                file_path = os.path.join(root, file)
                # Creats realtive path of file with os.path.relpath() function
                arcname = os.path.relpath(file_path, folder_path)
                # Write file to arcname
                archive.write(file_path, arcname=arcname)

    # Encrypt compressed folder
    with open(compressed_folder_path, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(compressed_folder_path, "wb") as file:
        file.write(encrypted_file)

    print(f"\nYou have successfully encrypted folder {folder_path}")

def decrypt_folder():
    exit

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
        print("1) Encrypt file\n2) Decrypt file\n3) Encrypt message string\n4) Decrypt message string\n5) Encrypt folder\n6) Decrypt folder\nexit) exit program")
        user_option = str(input("------------------------\n"))

        if user_option == "1":
            encrypt_file()
        elif user_option == "2":
            decrypt_file()
        elif user_option == "3":
            encrypt_string()
        elif user_option == "4":
            decrypt_string()
        elif user_option == "5":
            encrypt_folder()
        elif user_option == "6":
            decrypt_folder()
        elif user_option == "exit":
            print("\nExited successfully!\n")
            exit()
        else:
            print("\nInvalid input please try again!")
            continue

# End