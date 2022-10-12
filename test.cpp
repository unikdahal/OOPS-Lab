#include <iostream>
using namespace std;

class cube
{
public:
    int n;
    friend int Cube(cube c);
    int x;
};
int Cube(cube c)
{

    for (int i = 1; i <= c.n; i++)
    {
        c.x = i * i * i;
        cout << c.x << endl;
    }
}

int main()
{
    cube c;
    cout << "Enter the integer upto which cube is needed:" << endl;
    cin >> c.n;
    int Cube(c.n);
    return 0;
}
