#  For having the length of at least 4 character

import re

def retrieve_words_from_binary_file(file_path):
    # Read binary data from the file
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Decode binary data into a string using an appropriate encoding
    # For example, assuming UTF-8 encoding
    text = binary_data.decode('utf-8')

    # Define the regular expression pattern
    pattern = r'\b\w{4,}\b'

    # Use re.findall to find all matches in the text
    matches = re.findall(pattern, text)

    return matches

# Example usage
file_path = 'path/to/your/binary/file.bin'
result = retrieve_words_from_binary_file(file_path)

print(result)
