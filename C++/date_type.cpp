#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Creating auto variables
    auto myNum = 5; // int
    auto myFloatNum = 5.99; // float
    auto myDoubleNum = 9.98; // double
    auto myLetter = 'D'; // char
    auto myBoolean = true; // bool
    auto myString = string("Hello"); // std::string

    cout << "myNum: " << myNum << endl;
    cout << "myFloatNum: " << myFloatNum << endl;
    cout << "myDoubleNum: " << myDoubleNum << endl;
    cout << "myLetter: " << myLetter << endl;
    cout << "myBoolean: " << myBoolean << endl;
    cout << "myString: " << myString << endl;

    // Create variables of different data types
    int items = 50;
    double cost_per_item = 9.99;
    double total_cost = items * cost_per_item;
    char currency = '$';

    // Print variables
    cout << "Number of items: " << items << "\n";
    cout << "Cost per item: " << cost_per_item << currency << "\n";
    cout << "Total cost = " << total_cost << currency << "\n";

    return 0;
}
