# Extract email from the file

import re

def extract_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Define a regex pattern for matching emails
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        emails = re.findall(email_pattern, content)
        
        return emails

file_path = 'your_file.txt'
emails_found = extract_emails_from_file(file_path)

print("Extracted Emails:")
for email in emails_found:
    print(email)
