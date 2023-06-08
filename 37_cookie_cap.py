# Script: 37 - Cookie Capture Capades **INCOMPLETE**
# Author: Robert Gregor
# Date of latest revision: 07 JUN 23

# Objectives - Add code to make script perform the following:
    # Send the cookie back to the site and receive a HTTP response
    # Generate a .html file to capture the contents of the HTTP response
    # Open it with Firefox

# My Sources
    # [webbrowser — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html)
    # [https://docs.python.org/3/library/webbrowser.html](https://docs.python.org/3/library/webbrowser.html)
    # [Python File Write](https://www.w3schools.com/python/python_file_write.asp)
    # [Opening a site on Firefox using webbrowser module](https://stackoverflow.com/questions/23310513/opening-a-site-on-firefox-using-webbrowser-module)
    # [How to Open URL in Firefox Browser from Python Application?](https://pythonexamples.org/python-open-url-in-firefox-browser/)

#!/usr/bin/env python

import requests, webbrowser, os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send GET request and cookies to targetsite with request.get method
response = requests.get(targetsite, cookies=cookie)

# Opens response.html in write mode
with open('response.html', 'w') as f:
    # Write response contents to response.html file
    f.write(response.text)

# Declare variable equal to firefox path
firefox_path = '/usr/bin/firefox'
# Registers firefox to be used by imported browser module by default
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), -1)
# Use webbrowser module to open new firefox tab and navigate to response.html file
webbrowser.get('firefox').open_new_tab('file://' + os.path.realpath('response.html'))