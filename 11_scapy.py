# Script: 11 - Scapy (Part I)
# Author: Robert Gregor
# Date of latest revision: 01 MAY 23

# Objectives
    # In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
        # Utilize the scapy library, define host IP, define port range or specific set of ports to scan
        # Test each port in the specified range using a for loop
            # If flag 0x12 received, send a RST packet to graciously close the open connection
                # Notify the user the port is open.
            # If flag 0x14 received, notify user the port is closed.
            # If no flag is received, notify the user the port is filtered and silently dropped.

# Code Fellows Sources:
    # [Welcome to Scapy’s documentation!](https://scapy.readthedocs.io/en/latest/index.html)
    # [About Scapy](https://scapy.readthedocs.io/en/latest/introduction.html#)
    # [Build your own tools](https://scapy.readthedocs.io/en/latest/extending.html)

# My Sources:
    # [Port scanning using Scapy](https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/)
    # [Scapy Cheat Sheet](https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf)
    # [Scapy p.06 Sending and Receiving with Scapy](https://thepacketgeek.com/scapy/building-network-tools/part-06/)
    # [Requests and Responses](https://docs.scrapy.org/en/latest/topics/request-response.html)
    # [Scapy Usage](https://scapy.readthedocs.io/en/latest/usage.html)
    # [tuple() Function in Python](https://scapy.readthedocs.io/en/latest/usage.html)
    # [Python String split() Method](https://www.tutorialsteacher.com/python/string-split)
    # [Guide on the Python Map Function](https://www.bitdegree.org/learn/python-map)

#! /usr/bin/env python

# Import libraries
import sys
from scapy.all import IP, TCP, sr1, send

# Declares scan_ports function with two user supplied arguements
def scan_ports(host_name, port_range):
    # For loop used to iterate through user provided port range
    for port in range(port_range[0], port_range[1] + 1):
        # Sets host_name as IP destination, creates TCP packet, sets destination port, and sets SYN flag
        packet = IP(dst=host_name) / TCP(dport=port, flags="S")
        # Sends created packet and waits for reponse
        response = sr1(packet, timeout=1, verbose=0)
        # Conditional determines actions based on response, if no response filtered result is given
        if response is None:
            print(f"Appears port {port} is filtered (silently dropped)")
        # If response has TCP layer checks TCP flags
        elif response.haslayer(TCP):
            # Conditional determines if TCP flag is equal to 0x12
            if response[TCP].flags == 0x12:
                # Creates and sends packet with RST flag set to close connection
                send_rst = IP(dst=host_name) / TCP(dport=port, flags="R")
                send(send_rst, verbose=0)
                # Informs user of open port
                print(f"Port {port} is Open")
            # Conditional determines if TCP flag is equal to 0x14
            elif response[TCP].flags == 0x14:
                # Informs user of closed port
                print(f"Port {port} is closed")
        else:
            # Informs user of an unexpected response
            print(f"Port {port} provided an unexpected response")

while True:
      
        print("\n--------------------------------")
        print("Welcome to the tcp_port_scanner!")
        print("--------------------------------")

        # Sets variable based on user input
        host_name = input("\nPlease enter the host name you would like to scan (ex. scanme.nmap.org)")
        port_range_input = input("\nPlease enter the port range you would like to scan (ex. (100, 200)")

        # Converts user input into integer tuple
        port_range = tuple(map(int, port_range_input.split(', ')))
        # Execute scan_port function with two arguements
        scan_ports(host_name, port_range)

# End