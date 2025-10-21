// este es un ejemplo de comentario
/* este es otro ejemplo de comentario */

// Incluye la librería para entrada/salida
#include <iostream>
// Usa el espacio de nombres estándar
using namespace std;

// Función principal del programa
int main()
{
    // Declaración de variables
    int a, b;
    // Pide el primer número y almacena entrada en la variable a
    cout << "Ingresa el primer numero: " << endl;
    cin >> a;
    // Pide el segundo número y almacena entrada en la variable b
    cout << "Ingresa el segundo numero: " << endl;
    cin >> b;
    // Muestra las operaciones básicas
    cout << "La suma de los numeros es: " << a + b << endl;
    cout << "La resta de los numeros es: " << a - b << endl;
    cout << "La multiplicacion de los numeros es: " << a * b << endl;
    cout << "La division de los numeros es: " << a / b << endl;
    cout << "El residuo es: " << a % b << endl;

    // Pausa hasta ingresar cualquier tecla
    system("pause");
    return EXIT_SUCCESS;
}
