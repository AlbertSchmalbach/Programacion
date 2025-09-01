#include <iostream>
#include <string>
using namespace std;

int main()
{   
    // FOR
    for (int i = 0; i < 5; i++)
    {
        cout << "Valor: " << i << endl;
    }

    cout << endl;

    for (int i = 0; i < 5; i++)
    {   
        if (i == 3) continue;
        cout << "Valor: " << i << endl;
    }

    cout << endl;

    for (int i = 0; i < 5; i++)
    {   
        if (i == 3) break;
        cout << "Valor: " << i << endl;
    }

     cout << endl;

    // WHILE
    int c = 0;

    while (c <= 5)
    {
        cout << "Numero: " << c << endl;
        c++;
    }

     cout << endl;
    
    // DO WHILE

    int j = 0;

    do
    {
        cout << "Luz Saray" << endl;
        j++;
    } while (j <= 3);
    
     cout << endl;
    
    return 0;
}
