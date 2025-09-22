#include <iostream>
#include <string>
using namespace std;

int main()
{
    string cadena = "Contenido cadena";
    cout << cadena.length();
    cout << "\n";
    cout << cadena.size();
    cout << "\n";
    string firstname = "Albert ";
    string lastname = "Schmalbach";
    // string fullname = firstname + lastname;
    // string fullname = firstname + " " + lastname;
    string fullname = firstname.append(lastname);
    cout << fullname;
    return 0;
}
