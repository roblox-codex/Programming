#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    // seed the random number generator with the current time
    srand(time(NULL));

    // set the range of the lucky draw
    const int MIN_VALUE = 1;
    const int MAX_VALUE = 100;

    // generate a random number within the range
    int lucky_number = rand() % (MAX_VALUE - MIN_VALUE + 1) + MIN_VALUE;

    // display the lucky number
    cout << "The lucky number is: " << lucky_number << endl;

    return 0;
}
