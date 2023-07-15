#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Student class definition
class Student {
private:
    string name;
    int rollNumber;
    float marks;
public:
    Student(string n, int r, float m) {
        name = n;
        rollNumber = r;
        marks = m;
    }
    void display() {
        cout << "Name: " << name << endl;
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Marks: " << marks << endl;
        cout << "-------------------" << endl;
    }
    int getRollNumber() {
        return rollNumber;
    }
};

// Student Management System class definition
class StudentManagementSystem {
private:
    vector<Student> students;
public:
    void addStudent() {
        string name;
        int rollNumber;
        float marks;

        cout << "Enter name: ";
        cin.ignore();
        getline(cin, name);
        cout << "Enter roll number: ";
        cin >> rollNumber;
        cout << "Enter marks: ";
        cin >> marks;

        Student student(name, rollNumber, marks);
        students.push_back(student);

        cout << "Student record added successfully!" << endl;
    }

    void displayAllStudents() {
        if (students.empty()) {
            cout << "No student records found." << endl;
        } else {
            for (const auto& student : students) {
                student.display();
            }
        }
    }

    void searchStudent() {
        int rollNumber;
        bool found = false;

        cout << "Enter roll number to search: ";
        cin >> rollNumber;

        for (const auto& student : students) {
            if (student.getRollNumber() == rollNumber) {
                student.display();
                found = true;
                break;
            }
        }

        if (!found) {
            cout << "Student with roll number " << rollNumber << " not found." << endl;
        }
    }

    void deleteStudent() {
        int rollNumber;
        bool found = false;

        cout << "Enter roll number to delete: ";
        cin >> rollNumber;

        for (auto it = students.begin(); it != students.end(); ++it) {
            if (it->getRollNumber() == rollNumber) {
                students.erase(it);
                cout << "Student with roll number " << rollNumber << " deleted successfully!" << endl;
                found = true;
                break;
            }
        }

        if (!found) {
            cout << "Student with roll number " << rollNumber << " not found." << endl;
        }
    }
};

// Main function
int main() {
    StudentManagementSystem sms;
    int choice;

    do {
        cout << "----- Student Management System -----" << endl;
        cout << "1. Add Student" << endl;
        cout << "2. Display All Students" << endl;
        cout << "3. Search Student" << endl;
        cout << "4. Delete Student" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                sms.addStudent();
                break;
            case 2:
                sms.displayAllStudents();
                break;
            case 3:
                sms.searchStudent();
                break;
            case 4:
                sms.deleteStudent();
                break;
            case 5:
                cout << "Exiting the program..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }

        cout << endl;
    } while (choice != 5);

    return 0;
}
