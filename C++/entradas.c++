#include <iostream>
using namespace std;

int main()
{
    // int num1, num2;

    // cout << "Ingresa el primer numero: ";
    // cin >> num1;

    // cout << "Ingresa el segundo numero: ";
    // cin >> num2;
    // cout << endl;
    // cout << "Resultado division: " << num1 / num2 << endl;

    string name;
    cout << "Ingresa tu nombre: ";
    // cin >> name;
    getline(cin, name);

    cout << "Tu nombre es " << name << "\n";

    return 0;
}
