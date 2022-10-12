// 9. Create a class 'shape'. Derive three classes from it: Circle, Triangle and Rectangle. Include the relevant data members and functions in all the classes. Find the area of each shape and display it.

#include <iostream>
using namespace std;

class shape
{
public:
    virtual void area() = 0;
};

class circle : public shape
{
public:
    float r;
    void area()
    {
        cout << "Enter the radius of the circle: ";
        cin >> r;
        cout << "Area of the circle is: " << 3.14 * r * r << endl;
    }
};

class triangle : public shape
{
public:
    float b, h;
    void area()
    {
        cout << "Enter the base and height of the triangle: ";
        cin >> b >> h;
        cout << "Area of the triangle is: " << 0.5 * b * h << endl;
    }
};

class rectangle : public shape
{
public:
    float l, b;
    void area()
    {
        cout << "Enter the length and breadth of the rectangle: ";
        cin >> l >> b;
        cout << "Area of the rectangle is: " << l * b << endl;
    }
};

int main()
{
    shape *s;
    circle c;
    triangle t;
    rectangle r;
    s = &c;
    s->area();
    s = &t;
    s->area();
    s = &r;
    s->area();
    return 0;
}
