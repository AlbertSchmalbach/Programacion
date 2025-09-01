#include <iostream>
#include <string>
using namespace std;

int main()
{
    int edades[5] = {20, 42, 18, 30, 15};

    for (int i = 0; i <  5; i++)
    {
        cout << "Edad " << i+1 << " = " << edades[i] << endl;
    }

    cout << endl;

    string names[3];

    names[0] = "Alberto";
    names[1] = "Luz Saray";
    names[2] = "Misuris";

    for (string name : names)
    {
        cout << "Nombre: " << name << endl;
    }
    
    return 0;
}
