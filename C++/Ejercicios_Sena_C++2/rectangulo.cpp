#include <iostream>
using namespace std;

int main()
{   
    float area, a, b;
    cout << "*** AREA RECTANGULO ***"<<endl;
    // 𝐴 = 𝑎 𝑥 𝑏

    // entradas
    cout <<"Lado a"<<endl;
    cin >> a;

    cout << "Lado b"<<endl;
    cin >> b;

    // proceso
    area = a * b;

    // salida
    cout << "El area del rectangulo es: " << area << endl;

    return 0;
}
