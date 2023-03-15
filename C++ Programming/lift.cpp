#include <iostream>
using namespace std;

int main() {
   int current_floor = 0;
   int destination_floor = 0;

   // Get the current and destination floors from the user
   cout << "Enter the current floor: ";
   cin >> current_floor;

   cout << "Enter the destination floor: ";
   cin >> destination_floor;

   // Check if the user entered valid floor numbers
   if (current_floor < 0 || destination_floor < 0) {
      cout << "Invalid floor number" << endl;
      return 0;
   }

   // Move the lift up or down depending on the destination floor
   if (current_floor == destination_floor) {
      cout << "You are already on this floor" << endl;
   } else if (current_floor < destination_floor) {
      cout << "Moving up..." << endl;
      for (int i = current_floor; i < destination_floor; i++) {
         cout << "Floor " << i+1 << endl;
      }
      cout << "Reached destination floor " << destination_floor << endl;
   } else {
      cout << "Moving down..." << endl;
      for (int i = current_floor; i > destination_floor; i--) {
         cout << "Floor " << i-1 << endl;
      }
      cout << "Reached destination floor " << destination_floor << endl;
   }

   return 0;
}
