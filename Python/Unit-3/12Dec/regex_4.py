# Extract email from the file

import re

def extract_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Define a regex pattern for matching emails
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Use re.findall to find all matches in the content
        emails = re.findall(email_pattern, content)
        
        return emails

# Replace 'your_file.txt' with the actual path to your file
file_path = 'your_file.txt'
emails_found = extract_emails_from_file(file_path)

# Print the extracted emails
print("Extracted Emails:")
for email in emails_found:
    print(email)
