#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

string generatePassword(int length) {
    const string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?";
    const int charCount = characters.length();
    string password;

    srand(static_cast<unsigned int>(time(nullptr))); 

    for (int i = 0; i < length; ++i) {
        int index = rand() % charCount;
        password += characters[index]; 
    }

    return password;
}

int main() {
    int passwordLength;

    cout << "Random Password Generator" << endl;
    cout << "Enter the desired password length: ";
    cin >> passwordLength;

    if (passwordLength <= 0) {
        cout << "Invalid password length. Please enter a positive integer." << endl;
        return 1;
    }

    string password = generatePassword(passwordLength);

    cout << "Generated Password: " << password << endl;

    return 0;
}
