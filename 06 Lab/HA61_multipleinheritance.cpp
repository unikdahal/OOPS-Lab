// WAP to demonstrate the order of call of constructors and destructors in case of multiple
// inheritance.

#include<iostream>
using namespace std;

class A
{
public:
    A()
    {
        cout<<"A's constructor called"<<endl;
    }
    ~A()
    {
        cout<<"A's destructor called"<<endl;
    }
};

class B
{
public:
    B()
    {
        cout<<"B's constructor called"<<endl;
    }
    ~B()
    {
        cout<<"B's destructor called"<<endl;
    }
};

class C: public A, public B
{
public:
    C()
    {
        cout<<"C's constructor called"<<endl;
    }
    ~C()
    {
        cout<<"C's destructor called"<<endl;
    }
};

int main()
{
    C obj;
    return 0;
}


