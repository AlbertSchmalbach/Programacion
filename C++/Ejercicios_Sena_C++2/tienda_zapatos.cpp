#include <iostream>
#include <string>
using namespace std;

int main()
{
    string ref;
    string descp;
    int talla;
    char disponible_venta;
    double costo;
    double precio_venta;

    cout << "ADMINISTRAR VENTA DE ZAPATOS" <<endl;
    cout <<endl;

    // Entrada

    cout << "Digite la referencia del zapato..."<<endl;
    cin >> ref;
    cin.ignore();
    cout << "Digite la descripcion del zapato..."<<endl;
    getline(cin, descp);
    cout << "Digita la talla..."<<endl;
    cin>> talla;
    cout << "Digite con S/N si esta disponible para la venta..."<<endl;
    cin>> disponible_venta;
    cout << "Digite el costo del zapato..."<<endl;
    cin>> costo;
    cout << "Digite el precio de venta del zapato..."<<endl;
    cin >> precio_venta;

    cout <<endl;
    cout <<endl;

    // Salida
    cout << "LOS DATOS REGISTRADOS SON LOS SIGUIENTES: "<< endl;
    cout << "REFERENCIA: " << ref << endl;
    cout << "DESCRIPCION: " << descp << endl;
    cout << "TALLA: " << talla << endl;
    cout << "DISPONIBLE: " << disponible_venta << endl;
    cout << "COSTO: " << costo << endl;
    cout << "VENTA: " << precio_venta << endl;


    return 0;
}
