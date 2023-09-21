#include <iostream>
#include <cmath>

using namespace std;

// Triangle class
class Triangle {
public:
    // Function to calculate area of triangle using Heron's formula
    double area(double a, double b, double c) {
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
};

// Rectangle class
class Rectangle {
public:
    // Function to calculate area of rectangle
    double area(double length, double width) {
        return length * width;
    }
};

// Ellipse class
class Ellipse {
public:
    // Function to calculate area of ellipse
    double area(double major_axis, double minor_axis) {
        return 3.14159265358979323846 * major_axis * minor_axis;
    }
};

int main() {
    Triangle triangle;
    Rectangle rectangle;
    Ellipse ellipse;

    // Loop until the user chooses to exit
    while (true) {
        int choice;
        cout << "Select your shape:\n1. Triangle\n2. Rectangle\n3. Square\n4. Ellipse\n5. Circle\n6. Exit\nChoice: ";
        cin >> choice;

        // Exit the program if the user's choice is 6
        if (choice == 6) {
            break;
        }

        double a, b, c;
        switch (choice) {
            case 1:
                cout << "Enter lengths of three sides: ";
                cin >> a >> b >> c;
                cout << "The area of the triangle is " << triangle.area(a, b, c) << "\n";
                break;
            case 2:
                cout << "Enter length and width: ";
                cin >> a >> b;
                cout << "The area of the rectangle is " << rectangle.area(a, b) << "\n";
                break;
            case 3:
                cout << "Enter side length: ";
                cin >> a;
                cout << "The area of the square is " << rectangle.area(a, a) << "\n";
                break;
            case 4:
                cout << "Enter lengths of major and minor axes: ";
                cin >> a >> b;
                cout << "The area of the ellipse is " << ellipse.area(a, b) << "\n";
                break;
            case 5:
                cout << "Enter radius: ";
                cin >> a;
                cout << "The area of the circle is " << ellipse.area(a, a) << "\n";
                break;
        }
    }

    return 0;
}
