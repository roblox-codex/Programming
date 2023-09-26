import re

ip_address = input("Enter an IP address: ")

ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}'

if re.match(ipv4_pattern, ip_address):
    print("IPv4 address")
else:
    print("Not an IPv4 address")
