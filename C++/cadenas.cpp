#include <iostream>
#include <string>
using namespace std;

int main()
{
    string frase = "Amo a Luz Saray";
    string vocales = "aeiouAEIOU";
    int cant_vocal = 0;

    for (size_t i = 0; i < frase.length(); i++)
    {
        for (size_t j = 0; j < vocales.length() ; j++)
        {
            if (frase[i] == vocales[j])
            {
                cant_vocal += 1;
            }
        }
    }

    cout << "Cantidad de vocales: " << cant_vocal << endl;

    return 0;
}
