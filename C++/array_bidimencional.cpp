#include <iostream>
#include <string>
using namespace std;



int main()
{
    int matriz[3][3]{
        {12, 7, 8},
        {40, 18, 15},
        {12, 5, 80}
    };

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    

    return 0;
}
