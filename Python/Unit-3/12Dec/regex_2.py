# for single digit number from a string


import re

def retrieve_single_digit_numbers_from_binary_file(file_path):
    # Read binary data from the file
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Decode binary data into a string using an appropriate encoding
    # For example, assuming UTF-8 encoding
    text = binary_data.decode('utf-8')

    # Define the regular expression pattern for single-digit numbers
    pattern = r'\b\d\b'

    # Use re.findall to find all matches in the text
    matches = re.findall(pattern, text)

    return matches

# Example usage
file_path = 'path/to/your/binary/file.bin'
result = retrieve_single_digit_numbers_from_binary_file(file_path)

print(result)
