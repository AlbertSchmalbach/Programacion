
// Incluye la biblioteca estándar de entrada/salida
#include <iostream>
// Incluye la biblioteca para manejar cadenas de texto
#include <string>
// Permite usar los elementos de std sin anteponer 'std::'
using namespace std;


// Función que imprime un mensaje de bienvenida
void saludar()
{
    // Muestra el mensaje de bienvenida
    cout << "Hola, bienvenido a mi Calculadora." << endl;
    // Imprime una línea en blanco
    cout << endl;
}


// Función que imprime el menú de opciones de la calculadora
void imprimirMenu()
{
    // Muestra el título del menú
    cout << "=== Opciones Calculadora ===" << endl;
    cout << endl;
    // Muestra cada opción disponible
    cout << "1. Sumar." << endl;
    cout << "2. Restar." << endl;
    cout << "3. Multiplicar." << endl;
    cout << "4. Dividir." << endl;
    cout << "5. Salir." << endl;
    cout << endl;
}


// Función que suma dos números y retorna el resultado
int sumar(int a, int b)
{
    return a + b;
}

// Función que resta el segundo número al primero y retorna el resultado
int restar(int a, int b)
{
    return a - b;
}

// Función que multiplica dos números y retorna el resultado
int multiplicar(int a, int b)
{
    return a * b;
}

// Función que divide el primer número por el segundo y retorna el resultado
int dividir(int a, int b)
{
    if (b == 0)
    {   
        cout << "Error, division entre cero" << endl;
        return 0;
    }
    else
    {
        return a / b;
    }
    
    
}


// Función principal del programa
int main()
{
    int opcion; // Variable para almacenar la opción elegida por el usuario
    int a, b;   // Variables para los números a operar

    // Bucle principal que se repite hasta que el usuario elija salir (opción 5)
    while (opcion != 5)
    {
        saludar(); // Llama a la función de saludo
        imprimirMenu(); // Muestra el menú de opciones

        // Solicita al usuario que elija una opción
        cout << "Elija una opcion del menu: ";
        cin >> opcion;

        if (opcion != 5)
        {
        // Solicita el primer número
        cout << "Ingresa un primer numero: ";
        cin >> a;
        // Solicita el segundo número
        cout << "Ingresa un segundo numero: ";
        cin >> b;
        }
        else
        {   
            cout << endl;
            cout << "Saliendo de la calculadora..." << endl;
            continue;
        }
        

        // Evalúa la opción elegida usando switch
        switch (opcion)
        {
        case 1:
            // Suma los números y muestra el resultado
            cout << "Resultado Suma: " << sumar(a, b) << endl;
            cout << "=================================" << endl;
            cout << endl;
            break;
        case 2:
            // Resta los números y muestra el resultado
            cout << "Resultado Resta: " << restar(a, b) << endl;
            cout << "=================================" << endl;
            cout << endl;
            break;
        case 3:
            // Multiplica los números y muestra el resultado
            cout << "Resultado Multiplicacion: " << multiplicar(a, b) << endl;
            cout << "=================================" << endl;
            cout << endl;
            break;
        case 4:
            // Divide los números y muestra el resultado
            cout << "Resultado Division: " << dividir(a, b) << endl;
            cout << "=================================" << endl;
            cout << endl;
            break;

        default:
            // Maneja opciones no válidas
            cout << "Opcion no valida." << endl;
            cout << "=================================" << endl;
            cout << endl;
            break;
        }
    }

    return 0; // Fin del programa
}
