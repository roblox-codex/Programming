#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int count;
    ifstream infile("visitors.txt");
    infile >> count;
    infile.close();
    count++;
    ofstream outfile("visitors.txt");
    outfile << count;
    outfile.close();
    cout << "You are visitor #" << count << endl;
    return 0;
}
