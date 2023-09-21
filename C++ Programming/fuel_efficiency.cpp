#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Declare the necessary variables
    double gasPrices[4];   // Array to store the gas prices
    double avgPrice = 0.0; // Average price 
    double startMileage, endMileage, gallons;
    double totalMiles = 0.0, totalGallons = 0.0;
    double avgMilesPerGallon, cost;

    // Use a for loop to enter the price per gallon from four gas stations and calculate the average price
    for(int i=0; i<4; i++){
        cout << "Enter the price per gallon at station #" << i+1 << ": ";
        cin >> gasPrices[i];
        avgPrice += gasPrices[i];
    }
    avgPrice /= 4;

    // Use a while loop to enter the odometer readings and gallons purchased
    // The loop should repeatedly accumulate the number of miles traveled and number of gallons purchased
    char continueInput = 'y';
    while (continueInput == 'y' || continueInput == 'Y') {
        cout << "Enter the beginning odometer reading: ";
        cin >> startMileage;
        cout << "Enter the ending odometer reading: ";
        cin >> endMileage;
        cout << "Enter the gallons required for your fill-up: ";
        cin >> gallons;
        totalMiles += (endMileage - startMileage);
        totalGallons += gallons;
        cout << "Enter y to enter more readings or n to quit: ";
        cin >> continueInput;
    }

    // Calculate the car’s average miles per gallon
    avgMilesPerGallon = totalMiles / totalGallons;
    
    // Calculate the cost to take the car on a trip of 220 miles
    cost = (220 / avgMilesPerGallon) * avgPrice;

    // Determine the car's fuel efficiency
    string efficiency;
    if (avgMilesPerGallon <= 17) {
        efficiency = "Very inefficient";
    } else if (avgMilesPerGallon > 17 && avgMilesPerGallon <= 28) {
        efficiency = "OK";
    } else {
        efficiency = "Very efficient";
    }

    // Display the results with precision up to 2 decimal places
    cout << setprecision(2) << fixed;
    cout << "Average miles per gallon: " << avgMilesPerGallon << endl;
    cout << "Average price per gallon: $" << avgPrice << endl;
    cout << "Cost to drive the car 220 miles: $" << cost << endl;
    cout << "Fuel efficiency: " << efficiency << endl;

    return 0;
}
