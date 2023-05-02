# Script: 11 - Scapy (Part I) - INCOMPLETE
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

#! /usr/bin/env python

import sys
from scapy.all import srl,IP,ICMP

def scan_ports():
        
        exit

while True:
      
        print("\n----------------------------")
        print("Welcome to tcp_port_scanner!")
        print("----------------------------")

        host_ip = input("\nPlease enter the IP of the host you would like to scan")

        port_range = input("\nPlease enter the port range you would like to scan (ex 100-200)")

        scan_ports()

# End