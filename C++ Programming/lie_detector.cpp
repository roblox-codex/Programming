#include <iostream>
#include <string>

using namespace std;

int main() {
    string name;
    int age;
    bool isMarried;
    
    cout << "Welcome to the lie detector test." << endl;
    cout << "Please enter your name: ";
    cin >> name;
    cout << "Please enter your age: ";
    cin >> age;
    cout << "Are you married? (1 for yes, 0 for no): ";
    cin >> isMarried;
    
    if (age < 18) {
        cout << "You are too young to take this test." << endl;
    } else {
        cout << "Answer the following questions truthfully." << endl;
        
        string answer1, answer2;
        bool isLying = false;
        
        cout << "Question 1: Have you ever stolen something?" << endl;
        cin >> answer1;
        if (answer1 == "yes" && isMarried) {
            isLying = true;
        }
        
        cout << "Question 2: Have you ever lied to your spouse?" << endl;
        cin >> answer2;
        if (answer2 == "yes" && !isMarried) {
            isLying = true;
        }
        
        if (isLying) {
            cout << "You are lying!" << endl;
        } else {
            cout << "You are telling the truth." << endl;
        }
    }
    
    return 0;
}
