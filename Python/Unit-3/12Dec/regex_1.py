# For 3 or 4 or 5 char

import re

def retrieve_words_from_binary_file(file_path, min_length, max_length):
    # Read binary data from the file
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Decode binary data into a string using an appropriate encoding
    # For example, assuming UTF-8 encoding
    text = binary_data.decode('utf-8')

    # Define the regular expression pattern
    pattern = r'\b\w{' + str(min_length) + ',' + str(max_length) + r'}\b'

    # Use re.findall to find all matches in the text
    matches = re.findall(pattern, text)

    return matches

# Example usage
file_path = 'path/to/your/binary/file.bin'
min_length = 3
max_length = 5
result = retrieve_words_from_binary_file(file_path, min_length, max_length)

print(result)
