#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double gasPrices[4];
    double totalGasPrice = 0;
    double averageGasPrice;
    
    // Input gas prices using a for loop
    cout << "Enter the gas prices from four gas stations:" << endl;
    for (int i = 0; i < 4; i++) {
        cout << "Gas price at station " << (i + 1) << ": $";
        cin >> gasPrices[i];
        while (gasPrices[i] <= 0) {
            cout << "Gas price must be greater than zero. Enter a valid price: $";
            cin >> gasPrices[i];
        }
        totalGasPrice += gasPrices[i];
    }
    
    // Calculate average gas price
    averageGasPrice = totalGasPrice / 4.0;

    int odometerReading = 0;
    int previousOdometerReading = 0;
    double totalMiles = 0;
    double totalGallons = 0;
    double averageMilesPerGallon;
    
    // Input odometer readings and gallons purchased using a while loop
    cout << "Enter odometer readings and gallons purchased (Enter -1 to stop):" << endl;
    cin >> odometerReading;
    while (odometerReading != -1) {
        if (odometerReading <= previousOdometerReading) {
            cout << "Invalid odometer reading. It must be greater than the previous reading." << endl;
        } else {
            double gallons;
            cout << "Gallons purchased: ";
            cin >> gallons;
            
            while (gallons <= 0) {
                cout << "Gallons must be greater than zero. Enter a valid number of gallons: ";
                cin >> gallons;
            }
            
            totalMiles += odometerReading - previousOdometerReading;
            totalGallons += gallons;
            previousOdometerReading = odometerReading;
        }
        
        cout << "Enter odometer reading (or -1 to stop): ";
        cin >> odometerReading;
    }
    
    // Calculate average miles per gallon
    averageMilesPerGallon = totalMiles / totalGallons;

    // Calculate the cost to drive 220 miles
    double costFor220Miles = 220 / averageMilesPerGallon * averageGasPrice;

    // Display results
    cout << fixed << setprecision(2);
    cout << "\nAverage Price per Gallon: $" << averageGasPrice << endl;
    cout << "Average Miles per Gallon: " << averageMilesPerGallon << " mpg" << endl;
    cout << "Cost to drive 220 miles: $" << costFor220Miles << endl;
    
    // Determine fuel efficiency classification
    cout << "Fuel Efficiency Classification: ";
    if (averageMilesPerGallon > 28)
        cout << "Very Efficient" << endl;
    else if (averageMilesPerGallon > 17)
        cout << "OK" << endl;
    else
        cout << "Very Inefficient" << endl;

    return 0;
}
