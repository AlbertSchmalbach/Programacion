#include <iostream>
using namespace std;

void incrementar(int& num) {
    num++;
}

void cambiarSing(int& numero){
    numero = -numero;
}

int mult(int n1, int n2){
    return n1 * n2;
    
}

int main()
{
    int x = 10;
    int& ref = x;
    ref= 25;
    cout << x << endl;

    int valor = 2;
    incrementar(valor);
    cout << valor << endl;

    int a = 10;
    cambiarSing(a);
    cout << a << endl;

    int m = mult(12, 5);
    int& res = m;
    res = 30;

    cout << m << endl;


    return 0;
}
