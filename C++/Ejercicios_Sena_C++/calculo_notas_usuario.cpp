
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	cout << "Promedio de notas\n";
	cout << "Ingrese la cantidad de notas que desea digitar: ";

	int n = 0;
	while (!(cin >> n) || n <= 0) {
		cout << "Por favor ingrese un número entero mayor que 0: ";
		cin.clear();
	}

	double suma = 0.0;
	for (int i = 1; i <= n; ++i) {
		double nota = -1.0;
		while (true) {
			cout << "Ingrese la nota " << i << " (0.0 - 5.0): ";
			if (!(cin >> nota)) {
				cout << "Entrada inválida. Use un número con punto decimal si es necesario.\n";
				cin.clear();
				continue;
			}
			if (nota < 0.0 || nota > 5.0) {
				cout << "La nota debe estar entre 0.0 y 5.0. Intente nuevamente.\n";
				continue;
			}
			break;
		}
		suma += nota;
	}

	double promedio = suma / n;
	cout << fixed << setprecision(2);
	cout << "\nPromedio de las " << n << " notas: " << promedio << "\n";

	return 0;
}

