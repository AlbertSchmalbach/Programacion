#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    cout << "Ingrese un numero entero del 1 al 10." << endl;
    cin >> num;
    cout << "\n";

    cout << "Tabla de multiplicar del " << num << endl;

    for (size_t i = 1; i <= 10; i++)
    {   
        cout << num << " x " << i << " = " << num * i << endl;
    }

    return 0;
}
