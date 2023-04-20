# Script: 03 - Uptime Sensor Tool (Part 2)
# Author: Robert Gregor
# Date of latest revision: 19 APR 23

# Objectives
    # In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down
        # Transmit a single ICMP (ping) packet to a specific IP every two seconds
        # Evaluate the response as either success or failure
        # Assign success or failure to a status variable
        # For every ICMP transmission attempted, print status variable along with comprehensive timestamp and destination IP tested
            # Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
    # PART II - Add  below features to your uptime sensor tool
        # Ask user for email address and password to use for sending notifications
        # Send email to administrator if host status changes (from “up” to “down” or “down” to “up”)
        # Clearly indicate in message which host status changed, status before and after, and timestamp of event
    # Important Notes
        # DO NOT commit your email password in plain text within your script to GitHub as this easily becomes public.
        # Create a new “burner” account for this exercise. Do not use an existing email account.

# Stretch Goals (Optional Objectives)
    # In Python, add the below features to your uptime sensor tool
        # Save the output to a text file as a log of events
        # Accept user input for target IP address
    # PART II - Append all status changes to an event log
        # Each event must include timestamp, event code, any host IP involved, and a human readable description
    # PART II - Check for BURNER_EMAIL_ADDRESS and BURNER_EMAIL_PASSWORD environment variables (eg: loaded from .profile)
        # If found, script skips requesting credentials via user input
    # PART II - Alternatively, send notification email from cloud mailer service (like Mailgun, or AWS SES), instead of SMTP through burner address

# Code Fellows Sources
    # [How to print current date and time using Python?](https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python)
    # [Python time sleep() Method](https://www.tutorialspoint.com/python/time_sleep.htm)
    # [Python while Loop Statements](https://www.tutorialspoint.com/python/python_while_loop.htm)
    # [Python Ping: How to ping with Python](https://www.ictshore.com/python/python-ping-tutorial/)
    # [Ping 0.2: An implementation of ICMP ping in Python](https://pypi.org/project/ping/)
    # [How to Easily Automate Emails with Python](https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151)

# My Sources
    # [Python Looping Through a Range](https://www.w3schools.com/python/gloss_python_for_range.asp)
    # [Python append to a file](https://www.geeksforgeeks.org/python-append-to-a-file/)
    # [smtplib — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
    # [Sending Emails With Python](https://realpython.com/python-send-email/)
    # [mail.message: Representing an email message](https://docs.python.org/3/library/email.message.html)
    # [Python - Email Messages](https://www.tutorialspoint.com/python_network_programming/python_email_messages.htm)
    # [email.message.set_content('') not working and email shows no body](https://stackoverflow.com/questions/69486973/email-message-set-content-not-working-and-email-shows-no-body)

#!/usr/bin/env python3

# Main

import datetime
import click
import time
import smtplib
from pythonping import ping
from email.message import EmailMessage

def send_mail(admin_email, admin_pswd, subject, body):

    # Creates EmailMessage class, sets message content to body arguement, assigns Subject, From, and To headers to corresponding function arguements
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = admin_email
    msg['To'] = admin_email

    # Creates SMTP-SSL class, logs in to Gmail with user provided creds, sends email message, closes connection
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(admin_email, admin_pswd)
    server.send_message(msg)
    server.quit()

def ping_userIP(admin_email, admin_pswd, host_IP):

    # Declares ping_log variable equal to string, initializes last_status variable
    ping_log = "ping_log.txt"
    last_status = None

    # While loop used to ping user supplied IP
    while True:

        # Declares ping_result variable equal to output of ping command, declares current_time variable equal to current time
        ping_result = ping(host_IP, count=1, timeout=1)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Determines ping_status variable content case on ping_result.success() function return value
        if ping_result.success():
            ping_status = "UP"
        else:
            ping_status = "DOWN"

        # Conditional determines if status changed, if so determines content of email notification (subject, body), and calls send_mail function
        if last_status is not None and last_status != ping_status:
            subject = f"Host {host_IP} status changed"
            body = f"{current_time} - Host {host_IP} status changed from {last_status} to {ping_status}"
            send_mail(admin_email, admin_pswd, subject, body)

        # Stores current_time, ping_status, and user-IP variables as string in ping_entry variable and prints output to screen
        ping_entry = f"{current_time} - {ping_status} {host_IP}"
        print(ping_entry)

        # Creates ping_log.txt file, opens it in append mode, and writes/appends ping_entry variable contents to file
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
    print("\nTo exit the program at any prompt please type 'exit'")
    admin_email = str(input("\nPlease enter the Administrator's email address: "))
    admin_pswd = str(input("\nPlease enter the Administrator's password: "))
    host_IP = str(input("\nPlease enter the IP address of the host whose status you wish to monitor: "))
    print()

    # Conditional supporting exit functionality
    if host_IP == "exit":
        print("You have exited the uptime sensor program successfully!\n")
        exit()

    # Call the ping_userIP function with multiple arguements
    ping_userIP(admin_email, admin_pswd, host_IP)

    # Enter to return to IP input
    input("\nPress Enter to continue...")

# End