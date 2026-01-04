#include <iostream>
using namespace std;

void seleccionar_tabla(int n){
    for (size_t i = 0; i <= 10; i++)
    {
        cout << n << " x " << i  << " = " << n*i << endl;
    }
}

int main()
{   
    int num;

    while (true)
    {
        cout << "Seleccione una tabla de multiplicacion: " << endl;
        cin >> num;

        cout <<endl;

        cout << "TABLA DE MULTIPLICAR DEL  " << num << endl;
        cout <<endl;
        seleccionar_tabla(num);
        cout <<endl;
        cout << "Alberto Schmalbach - ESTRUCTURA DEL LENGUAJE DE PROGRAMACION C++ (NIVEL I) (3397464)" << endl;
        cout <<endl;
    }

    return 0;
}



