#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    float area, r;
    const float pi = 3.1416;

    cout << "*** AREA CIRCULO ***" << endl;
    // 𝐴 = 𝜋𝑟2

    // entrada
    cout << "Digite el valor del radio: "<< endl;
    cin >> r;

    // proceso
    area = pi*(pow(r, 2));

    // salida
    cout << "El area del circulo es: " << area << endl;

    return 0;
}
