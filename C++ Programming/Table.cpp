#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Create a 2D array to store the table data
    int table[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

    // Print the table header
    cout << setw(10) << "Column 1" << setw(10) << "Column 2" << setw(10) << "Column 3" << setw(10) << "Column 4" << endl;

    // Print the table data
    for (int i = 0; i < 3; i++) {
        cout << setw(10) << table[i][0] << setw(10) << table[i][1] << setw(10) << table[i][2] << setw(10) << table[i][3] << endl;
    }

    return 0;
}
