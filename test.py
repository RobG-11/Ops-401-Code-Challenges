#!/usr/bin/env python3

import datetime
import click
import time
import smtplib
from pythonping import ping
from email.message import EmailMessage
from getpass import getpass

email = input("Email: ")
password = getpass("Password: ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
server.sendmail("heartbeat@bot.com", email, "server on fire")
server.quit
