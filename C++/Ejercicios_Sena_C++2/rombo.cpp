#include <iostream>
using namespace std;

int main()
{   
    float area, D, d;
    cout << "*** AREA ROMBO ***"<<endl;
    // 𝐴 = D 𝑥 d / 2

    // entradas
    cout <<"D: "<<endl;
    cin >> D;

    cout << "d: "<<endl;
    cin >> d;

    // proceso
    area = D * d / 2;

    // salida
    cout << "El area del rombo es: " << area << endl;

    return 0;
}
