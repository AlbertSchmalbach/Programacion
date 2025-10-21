// 𝑎=(𝑣𝑒𝑙𝑜𝑐𝑖𝑑𝑎𝑑 𝑓𝑖𝑛𝑎𝑙−𝑣𝑒𝑙𝑜𝑐𝑖𝑑𝑎𝑑 𝑖𝑛𝑖𝑐𝑖𝑎𝑙)/𝑡𝑖𝑒𝑚𝑝𝑜

#include <iostream>
#include <string>
using namespace std;

// Ejercicio: Un carro parte del reposo y alcanza una velocidad de 20 m/s en 5 segundos.

int main()
{

    const int v_ini = 0;

    int v_final, t, a;

    cout << "Ingrese el valor de la velocidad final en metros: ";
    cin >> v_final;
    cout << "\n";

    cout << "Ingrese el tiempo del recorrido en segundos: ";
    cin >> t;
    cout << "\n";

    a = (v_final - v_ini) / t;

    cout << " La aceleracion del vehiculo es: " << a  << " m/s2." << endl;

    return 0;
}
