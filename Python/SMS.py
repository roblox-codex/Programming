import datetime
import smtplib

class Student:
    def __init__(self, name, phone_number, book_name, due_date):
        self.name = name
        self.phone_number = phone_number
        self.book_name = book_name
        self.due_date = due_date

    def check_due_date(self):
        if datetime.datetime.now() > self.due_date:
            return True
        return False

    def send_reminder(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("02singhdigvijay@gmail.com", "robloxcodex")
        message = f"Reminder: Your library book, {self.book_name}, is overdue. Please return it as soon as possible."
        server.sendmail("your_email@gmail.com", self.phone_number, message)
        server.quit()

student_list = []

# Add students to the list
student_list.append(Student("John Smith", "+1234567890", "The Great Gatsby", datetime.datetime(2021, 12, 1)))
student_list.append(Student("Jane Doe", "+0987654321", "To Kill a Mockingbird", datetime.datetime(2022, 1, 15)))

for student in student_list:
    if student.check_due_date():
        student.send_reminder()
