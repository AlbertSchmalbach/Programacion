#include <iostream>
using namespace std;

int main()
{
    float area, B, b, h;

    cout << "*** AREA TRAPECIO ***" << endl;
    // 𝐴 = (B 𝑥 b / 2) 𝑥 h

    // entradas
    cout << "Lado B" << endl;
    cin >> B;

    cout << "Lado b" << endl;
    cin >> b;

    cout << "Lado h" << endl;
    cin >> h;

    // proceso
    area = (B * b / 2) * h;

    // salida
    cout << "El area del trapecio es: " << area << endl;

    return 0;
}
