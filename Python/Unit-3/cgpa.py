def calculate_cgpa():

    num_subjects = int(input("Enter the number of subjects: "))

    total_grade_points = 0
    total_credit_hours = 0

    for i in range(1, num_subjects + 1):

        grade = input(f"Enter the grade for Subject {i}: ").upper()
        credit_hours = float(input(f"Enter the credit hours for Subject {i}: "))

        if grade == 'A':
            grade_points = 4.0
        elif grade == 'B':
            grade_points = 3.0
        elif grade == 'C':
            grade_points = 2.0
        elif grade == 'D':
            grade_points = 1.0
        elif grade == 'F':
            grade_points = 0.0
        else:
            print("Invalid grade entered. Please enter A, B, C, D, or F.")
            return

        total_grade_points += grade_points * credit_hours
        total_credit_hours += credit_hours

    cgpa = total_grade_points / total_credit_hours

    print(f"CGPA: {cgpa:.2f}")

calculate_cgpa()
