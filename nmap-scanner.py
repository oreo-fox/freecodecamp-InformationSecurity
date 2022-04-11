from ipaddress import ip_address
import nmap

scanner = nmap.PortScanner()

ip_address = input("Enter IP address: \n")

option = input("""  1) SYN ACK Scan
                    2)UDP Scan
                    3) Comprehensive Scan \n""")

if option == 1:
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports: ", scanner[ip_address]['tcp'].keys())

elif option == 2:
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports: ", scanner[ip_address]['udp'].keys())

elif option == 3:
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open ports: ", scanner[ip_address]['tcp'].keys())

else:
    print("option not valid")
