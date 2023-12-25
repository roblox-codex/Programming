import re

def validate_mac_address(mac_address):
    mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(mac_pattern, mac_address) is not None

def validate_ipv6_address(ipv6_address):
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})$|^:((:[0-9a-fA-F]{1,4}){1,7})$|^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}%[0-9a-zA-Z]{1,}$|^([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}%[0-9a-zA-Z]{1,}$|^([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}%[0-9a-zA-Z]{1,}$|^([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}%[0-9a-zA-Z]{1,}$|^([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}%[0-9a-zA-Z]{1,}$|^([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}%[0-9a-zA-Z]{1,}$|^[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})%[0-9a-zA-Z]{1,}$|^:((:[0-9a-fA-F]{1,4}){1,7})%[0-9a-zA-Z]{1,}$'
    return re.match(ipv6_pattern, ipv6_address) is not None

user_input_mac = input("Enter a MAC address: ")
user_input_ipv6 = input("Enter an IPv6 address: ")

if validate_mac_address(user_input_mac):
    print(f"{user_input_mac} is a valid MAC address.")
else:
    print(f"{user_input_mac} is not a valid MAC address.")

if validate_ipv6_address(user_input_ipv6):
    print(f"{user_input_ipv6} is a valid IPv6 address.")
else:
    print(f"{user_input_ipv6} is not a valid IPv6 address.")
