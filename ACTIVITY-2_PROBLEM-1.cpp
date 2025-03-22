#include <iostream>
using namespace std;

int main()
{
    int a[3] = {89, 26, 7};
    int b[3] = {89, 26, 7};
    int chef1Points = 0, chef2Points = 0;

    for (int i = 0; i < 3; i++)
    {
        if (a[i] > b[i])
        {
            chef1Points++;
        }
        else if (a[i] < b[i])
        {
            chef2Points++;
        }
    }

    cout << chef1Points << " " << chef2Points << endl;
    if (chef1Points == chef2Points)
    {
        cout << "--- TIE , THERE IS NO ONE WINNER ---";
    }
    else if (chef1Points < chef2Points)
    {
        cout << "---- HURREY, CHEF-> 2 IS WINNER ----";
    }
    else
    {
        cout << "---- HURREY, CHEF-> 1 IS WINNER ----";
    }
    return 0;
}
