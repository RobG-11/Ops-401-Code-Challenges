# Script: 11 - Scapy (Part II) - INCOMPLETE
# Author: Robert Gregor
# Date of latest revision: 02 MAY 23

# Objectives (PART I)
    # In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
        # Utilize the scapy library, define host IP, define port range or specific set of ports to scan
        # Test each port in the specified range using a for loop
            # If flag 0x12 received, send a RST packet to graciously close the open connection
                # Notify the user the port is open.
            # If flag 0x14 received, notify user the port is closed.
            # If no flag is received, notify the user the port is filtered and silently dropped.
# Objectives (PART II)
    # Add the following features to your Network Security Tool:
        # 


# Code Fellows Sources:
    # [Welcome to Scapy’s documentation!](https://scapy.readthedocs.io/en/latest/index.html)
    # [About Scapy](https://scapy.readthedocs.io/en/latest/introduction.html#)
    # [Build your own tools](https://scapy.readthedocs.io/en/latest/extending.html)
# Code Fellows Sources (PART II):
    # [Generating a Range of IP Addresses from a CIDR Address in Python] - BAD LINK

# My Sources (PART I):
    # [Port scanning using Scapy](https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/)
    # [Scapy Cheat Sheet](https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf)
    # [Scapy p.06 Sending and Receiving with Scapy](https://thepacketgeek.com/scapy/building-network-tools/part-06/)
    # [Requests and Responses](https://docs.scrapy.org/en/latest/topics/request-response.html)
    # [Scapy Usage](https://scapy.readthedocs.io/en/latest/usage.html)
    # [tuple() Function in Python](https://scapy.readthedocs.io/en/latest/usage.html)
    # [Python String split() Method](https://www.tutorialsteacher.com/python/string-split)
    # [Guide on the Python Map Function](https://www.bitdegree.org/learn/python-map)
# My Sources (PART II)
    # User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode
    # ICMP Ping Sweep tool
        # Prompt user for network address including CIDR block, for example “10.10.0.0/24”
            # Careful not to populate the host bits!
        # Create a list of all addresses in the given network
        # Ping all addresses on the given network except for network address and broadcast address
            # If no response, inform the user that the host is down or unresponsive
            # If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13, inform user host is actively blocking ICMP
            # Otherwise, inform the user that the host is responding
        # Count how many hosts are online and inform the user

#! /usr/bin/env python

# Import libraries
import sys
from scapy.all import IP, TCP, sr1, send

# Declares scan_ports function with two user supplied arguements
def scan_ports(host_name, port_range):

    # Sets variables based on user input
    host_name = input("\nPlease enter the host name you would like to scan (ex. scanme.nmap.org)")
    port_range_input = input("\nPlease enter the port range you would like to scan (ex. (100, 200)")

    # Converts user input into integer tuple
    port_range = tuple(map(int, port_range_input.split(', ')))
    
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

def icmp_ping_sweep():
    exit()

while True:
      
    print("\n------------------------")
    print("Please choose an option:")
    print("------------------------")
    print("1) Automated Port Scanner\n2) ICMP Ping Sweep\nexit) exit program")
    user_option = str(input("------------------------\n"))

    if user_option == "1":
        scan_ports()
    elif user_option == "2":
        icmp_ping_sweep()
    elif user_option == "exit":
        print("\nExited successfully!\n")
        exit()
    else:
        print("\nInvalid input please try again!")
        continue

# End