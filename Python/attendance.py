# define a list of students
students = ['Aniket', 'Aviral', 'Satty', 'Sarang', 'Rupa']

# initialize an empty dictionary to store attendance
attendance = {}

# loop through each student
for student in students:
    # prompt the user to enter attendance for the student
    print(f"Is {student} present? (y/n)")
    response = input().lower()
    
    # validate the user input
    while response not in ['y', 'n']:
        print("Invalid response. Please enter y or n.")
        response = input().lower()
    
    # store the attendance for the student in the dictionary
    if response == 'y':
        attendance[student] = 'Present'
    else:
        attendance[student] = 'Absent'
    
# print the attendance report
print("\nAttendance Report")
for student, status in attendance.items():
    print(f"{student}: {status}")
