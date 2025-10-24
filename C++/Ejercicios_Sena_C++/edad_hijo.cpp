// Incluye la librería para entrada/salida
#include <iostream>
// Usa el espacio de nombres estándar
using namespace std;

int main()
{
    int edad;
    cout << "Cual es la edad de su hijo: ";
    cin >> edad;

    if (edad > 0 && edad < 6)
    {
        cout<< "El niño pertenece al grupo de primera infancia" << endl;
    }
    else if (edad >= 6 && edad < 12)
    {
        cout<< "El niño pertenece al grupo de la segunda infancia" << endl;
    }
    else
    {
        cout << "pertenece al grupo de los adolescentes" << endl;
    }
    

    return 0;
}
