// 1.WAP to swap private data member of two classes.
// [The classes have no relation with each other].
#include<iostream>
using namespace std;
class B;
class A
{
    private:
        int num1;
    public:
        A()
        {
            cout<<"Enter the value of num1: ";
            cin>>num1;

        }
        void show()
        {
                cout<<"\n Value of Number 1 : "<<num1;
        }
        friend void swap(A *num1, B *num2);
};
class B
{
    private:
        int num2;
    public:
        B()
        {
            cout<<"Enter the value of num2: ";
            cin>>num2;
        }
        void show()
        {
                cout<<"\n Value of Number 2 : "<<num2;
        }
        friend void swap(A *num1, B *num2);
};
void swap(A *no1, B *no2)
{
        int no3;
        no3=no1->num1;
        no1->num1=no2->num2;
        no2->num2=no3;
}
int main()
{
        A b;
        B d;
        swap(&b, &d);
        b.show();
        d.show();
        return 0;
}
