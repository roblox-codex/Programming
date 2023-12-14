import re

def extract_mobile_numbers(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Define a regex pattern for matching mobile numbers with country code (1-3 digits)
        mobile_pattern = r'\b(?:\+\d{1,3}\s?)?\d{10}\b'

        mobile_numbers = re.findall(mobile_pattern, content)
        
        return mobile_numbers

file_path = 'your_file.txt'
mobile_numbers_found = extract_mobile_numbers(file_path)

print("Extracted Mobile Numbers:")
for number in mobile_numbers_found:
    print(number)
