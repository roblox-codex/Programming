import datetime

# Take input from user
date_str = input("Enter date (in dd/mm/yyyy format): ")

# Convert input string to datetime object
date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')

# Get day of the week
day = date_obj.strftime('%A')

# Output the day
print("The day is:", day)
