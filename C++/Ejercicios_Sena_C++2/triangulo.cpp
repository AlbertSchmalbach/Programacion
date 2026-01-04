#include <iostream>
using namespace std;

int main()
{   
    float area, b, h;
    cout << "*** AREA TRIANGULO ***"<<endl;
    // 𝐴 = b 𝑥 h / 2

    // entradas
    cout <<"Lado b"<<endl;
    cin >> b;

    cout << "Lado h"<<endl;
    cin >> h;

    // proceso
    area = b * h / 2;

    // salida
    cout << "El area del triangulo es: " << area << endl;

    return 0;
}
