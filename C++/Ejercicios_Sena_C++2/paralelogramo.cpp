#include <iostream>
using namespace std;

int main()
{   
    float area, b, h;
    cout << "*** AREA PARALELOGRAMO ***"<<endl;
    // 𝐴 = b 𝑥 h 

    // entradas
    cout <<"Lado b"<<endl;
    cin >> b;

    cout << "Lado h"<<endl;
    cin >> h;

    // proceso
    area = b * h;

    // salida
    cout << "El area del paralelogramo es: " << area << endl;

    return 0;
}
