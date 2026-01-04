#include <iostream>
using namespace std;

int suma(int num1, int num2);

int main()
{
    int a, b;
    cout << "Ingresa el primer numero: " << endl;
    cin >> a;

    cout << "Ingresa el segundo numero: " << endl;
    cin >> b;

    cout << "El resultado de la suma es: " << suma(a, b) << endl;
    system("pause");

    return EXIT_SUCCESS;
}

int suma(int num1, int num2)
{
    return num1 + num2;
}