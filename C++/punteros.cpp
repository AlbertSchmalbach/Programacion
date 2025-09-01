
// Incluye la biblioteca estándar de entrada/salida
#include <iostream>
// Incluye la biblioteca para manejar cadenas de texto
#include <string>
// Permite usar los elementos de std sin anteponer 'std::'
using namespace std;


int main()
{
    int x = 12; 
    int* p = &x; // Declara un puntero a entero y lo inicializa con la dirección de x
    cout << *p << endl; // Imprime el valor al que apunta p (contenido de x)

    *p = 24; // Cambia el valor de x a través del puntero p

    cout << x << endl; // Imprime el nuevo valor de x

    char letra = 'A'; 
    char* ptr = &letra; // Declara un puntero a char y lo inicializa con la dirección de letra
    cout << *ptr << endl; // Imprime el valor al que apunta ptr (contenido de letra)

    int numeros[] = {5, 12, 8}; 
    int* pt = numeros; // Declara un puntero a entero y lo inicializa con la dirección del primer elemento del arreglo
    cout << *(pt + 1) << endl; // Imprime el segundo elemento del arreglo usando aritmética de punteros

    return 0; // Fin del programa
}
