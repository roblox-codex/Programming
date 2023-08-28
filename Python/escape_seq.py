# Printing a single backslash
print("This is a single backslash: \\")

# Creating file paths (Windows example)
file_path = "C:\\Users\\Username\\Documents\\file.txt"
print("File path:", file_path)

# Creating regular expressions
import re
pattern = r"\d{3}-\d{2}-\d{4}"
text = "Social Security Number: 123-45-6789"
match = re.search(pattern, text)
if match:
    print("Found SSN:", match.group())
else:
    print("No SSN found.")
