# Script: 38 - XSS Vulnerability Detection with Python **COMPLETE**
# Revised By: Robert Gregor
# Date of latest revision: 08 JUN 23

# Objectives - Programmatically detect presence (or lack) of XSS vulnerability in given target URL using Python

# Requirements - Copy DEMO.md file from class repo > class-38 > challenges and complete TODOs
    # Fully annotate any missing comments and populate any missing variables/code
    # Test the script in Web Security Dojo to confirm the output is correct
        # Target URL should yield positive vuln detection: https://xss-game.appspot.com/level1/frame
        # Target URL should yield a negative vuln detection: http://dvwa.local/login.php

# My Sources
    # [How to Build a SQL Injection Scanner in Python](https://www.thepythoncode.com/article/sql-injection-vulnerability-detector-in-python)

#!/usr/bin/env python

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###

# Retrieves all form elements from provided url parameter
    # Parses information and stores in variable
    # Returns list of forms

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###

# Retrieves form details from provided form parameter
    # Declares dictionary to store form details extracted from element list
    # Declares list to store element details
    # Returns detail dictionary with action, method, and inputs included

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: Add function explanation here ###

# Submit modified form and return server response
    # Create URL for form submission
    # Create dictionary to store specified input values

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###

# Conduct vulnerability scan
    # Retrieves all forms and prints total
    # Establishes script to use to test form fields
    # Submit form with javascript in text fields and store server reponse in content variable
    # Determine if java script is reflected in server reponse

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS Permitted!!!')</script>" ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Add main explanation here ###

# Ensures script is only executed when run directly
    # Requests user input for url
    # Prints results of scan_xss function executed with user provided url

### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearly indicating which is positive detection and negative detection

# dojo@dojo-VirtualBox:~/Desktop/class-38$ sudo python3 xss_scan.py
# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': "<script>alert('XSS Permitted!!!')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# True

# dojo@dojo-VirtualBox:~/Desktop/class-38$ sudo python3 xss_scan.py
# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/login.php.
# False
