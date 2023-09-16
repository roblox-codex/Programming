// 1-d Array

#include <iostream>

using namespace std;

int main() {
    const int size = 5;
    int arr[size];

    cout << "Enter " << size << " elements for the 1D array:" << endl;
    for (int i = 0; i < size; ++i) {
        cin >> arr[i];
    }

    return 0;
}



// 2-d Array

#include <iostream>

using namespace std;

int main() {
    const int rows = 3;
    const int cols = 3;
    int arr[rows][cols];

    cout << "Enter " << rows << " rows and " << cols << " columns of elements for the 2D array:" << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cin >> arr[i][j];
        }
    }

    return 0;
}
