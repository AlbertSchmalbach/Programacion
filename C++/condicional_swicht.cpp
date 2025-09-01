#include <iostream>
#include <string>
using namespace std;

int main()
{
    int opcion = 3;

    switch (opcion)
    {
    case 1:
        cout << "Excelente" << endl;
        break;

    case 2:
        cout << "Bueno" << endl;
        break;

    case 3:
        cout << "Regular" << endl;
        break;
    
    default:
         cout << "Malo" << endl;
        break;
    }
    
    return 0;
}
