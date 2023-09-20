#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

struct Item {
    string name;
    double price;
};

double calculateTotalCost(const vector<Item>& items, double taxRate) {
    double totalCost = 0.0;
    for (const Item& item : items) {
        totalCost += item.price;
    }
    return totalCost + (totalCost * taxRate);
}

int main() {
    vector<Item> shoppingList;
    double taxRate;

    cout << "Welcome to the Daily Life Shopping Calculator!" << endl;
    cout << "Enter the tax rate (e.g., 0.08 for 8%): ";
    cin >> taxRate;

    int itemCount;
    cout << "Enter the number of items in your shopping list: ";
    cin >> itemCount;

    for (int i = 0; i < itemCount; ++i) {
        Item item;
        cout << "Enter the name of item #" << i + 1 << ": ";
        cin >> item.name;
        cout << "Enter the price of item #" << i + 1 << ": $";
        cin >> item.price;
        shoppingList.push_back(item);
    }

    double totalCost = calculateTotalCost(shoppingList, taxRate);

    cout << fixed << setprecision(2);
    cout << "---------------------------" << endl;
    cout << "Shopping List:" << endl;
    for (const Item& item : shoppingList) {
        cout << item.name << ": $" << item.price << endl;
    }
    cout << "---------------------------" << endl;
    cout << "Total Cost (including tax): $" << totalCost << endl;

    return 0;
}
