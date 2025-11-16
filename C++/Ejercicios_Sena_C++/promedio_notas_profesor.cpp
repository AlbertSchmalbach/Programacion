#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    // Alberto Schmalbach Lopez - CONCEPTUALIZACION DEL LENGUAJE DE PROGRAMACION C++ (3351034)
    cout << "Promedio de 4 notas por estudiante\n";

    int continuar = 1; // 1 = continuar, 0 = terminar
    while (continuar == 1) {
        float nota1 = -1.0f, nota2 = -1.0f, nota3 = -1.0f, nota4 = -1.0f;

        // Entrada y validación para cada nota (0.0 - 5.0)
        cout << "Ingrese la primera nota (0.0 - 5.0): ";
        while (!(cin >> nota1) || nota1 < 0.0f || nota1 > 5.0f) {
            cout << "Valor inválido. Ingrese un número entre 0.0 y 5.0: ";
            cin.clear();
        }

        cout << "Ingrese la segunda nota (0.0 - 5.0): ";
        while (!(cin >> nota2) || nota2 < 0.0f || nota2 > 5.0f) {
            cout << "Valor inválido. Ingrese un número entre 0.0 y 5.0: ";
            cin.clear();
        }

        cout << "Ingrese la tercera nota (0.0 - 5.0): ";
        while (!(cin >> nota3) || nota3 < 0.0f || nota3 > 5.0f) {
            cout << "Valor inválido. Ingrese un número entre 0.0 y 5.0: ";
            cin.clear();
        }

        cout << "Ingrese la cuarta nota (0.0 - 5.0): ";
        while (!(cin >> nota4) || nota4 < 0.0f || nota4 > 5.0f) {
            cout << "Valor inválido. Ingrese un número entre 0.0 y 5.0: ";
            cin.clear();
        }

        float prom_nota = (nota1 + nota2 + nota3 + nota4) / 4.0f;

        cout << fixed << setprecision(2);
        cout << "\nPromedio: " << prom_nota << "\n";

        if (prom_nota >= 3.5f)
        {
            cout << "Resultado: Aprobado\n";
        }
        else if (prom_nota >= 3.0f && prom_nota < 3.5f)
        {
            cout << "Resultado: Recuperación posible (no aprobado actualmente)\n";
        }
        else
        {
            cout << "Resultado: No aprobado\n";
        }

        // Preguntar si desea procesar otro estudiante
        cout << "\n¿Desea digitar las notas de otro estudiante? (1 = sí, 0 = no): ";
        while (!(cin >> continuar) || (continuar != 0 && continuar != 1)) {
            cout << "Entrada inválida. Digite 1 para continuar o 0 para terminar: ";
            cin.clear();
        }
        cout << "\n";
    }

    cout << "Ejecución terminada.\n";
    return 0;
}
