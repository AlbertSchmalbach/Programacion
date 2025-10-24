#include <iostream>
using namespace std;

int main()
{
    float nota1, nota2, nota3, nota4, prom_nota;

    cout << "Ingrese la primera nota: ";
    cin >> nota1;

    cout << "\n";

    cout << "Ingrese la segunda nota: ";
    cin >> nota2;

    cout << "\n";

    cout << "Ingrese la tercera nota: ";
    cin >> nota3;

    cout << "\n";

    cout << "Ingrese la cuarta nota: ";
    cin >> nota4;

    cout << "\n";

    prom_nota = (nota1 + nota2 + nota3 + nota4) / 4;

    if (prom_nota >= 3.5)
    {
        cout << "Aprobado";
    }
    else if (prom_nota >= 3 && prom_nota < 3.5)
    {
        cout << "En este momento no tiene aprobada la materia de tecnología, pero tiene la oportunidad de recuperar";
    }
    else
    {
        cout << "No aprobado";
    }

    return 0;
}


// Alberto Schmalbach Lopez - CONCEPTUALIZACION DEL LENGUAJE DE PROGRAMACION C++ (3351034)
