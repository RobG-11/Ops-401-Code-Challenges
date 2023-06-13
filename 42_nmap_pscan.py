# Script: 42 - Attack Tools Part 2 of 3 **COMPLETE**
# Revised By: Robert Gregor
# Date of latest revision: 13 JUN 23

# Objectives - Use Python to develop a custom Nmap scanner that can later be combined with other Python scripts to create a pentester toolkit

#!/usr/bin/python3

import nmap, os

scanner = nmap.PortScanner()

while True:
    os.system('clear')
    print("Nmap Automation Tool")
    print("--------------------")

    ip_addr = input("IP address to scan: ")
    print("The IP you entered is: ", ip_addr)
    type(ip_addr)

    resp = input("""\nSelect scan to execute:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Aggressive Scan
                    4) Exit program\n""")
    print("You have selected option: ", resp)

    if resp == '4':
        exit

    ### TODO: Prompt the user to type in a port range for this tool to scan
    port_range = input("Enter port range to scan (e.g. 1-50): ")
    print("\nPort range is: \n", port_range)

    if resp == '1':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, port_range, '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
        input("\nResults can be seen above, press ENTER to return to main menu...")
    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, port_range, '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
        input("\nResults can be seen above, press ENTER to return to main menu...")
    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, port_range, '-v -A')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        if 'tcp' in scanner[ip_addr].all_protocols():
            print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
        if 'udp' in scanner[ip_addr].all_protocols():
            print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
        input("\nResults can be seen above, press ENTER to return to main menu...")