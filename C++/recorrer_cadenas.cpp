#include <iostream>
#include <string>
using namespace std;

int main()
{
    string myString = "Programar";
    cout << "Primer de caracter: " << myString[0] << endl;
    myString[myString.length()-1]= 's';
    cout << "Ultimo caracter: " << myString[myString.length() - 1] << "\n";

    // Otra forma de acceder
    cout << myString.at(5) << endl;

    return 0;
}
