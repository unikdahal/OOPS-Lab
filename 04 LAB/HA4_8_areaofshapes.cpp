//Find the Area of shapes using function overloading

#include<iostream>
using namespace std;

class Area{
    public:
        int a;
        int b;
        int c;
        int r;
        void getData(){
            cout<<"Enter the length \n";
            cin>>a;
            cout<<"Enter the breadth \n";
            cin>>b;
            cout<<"Enter the height \n";
            cin>>c;
            cout<<"Enter the radius \n";
            cin>>r;
        }
        void area(int a,int b){
            cout<<"The area of rectangle is "<<a*b<<endl;
            cout<<"The area of square is "<<a*a<<endl;
        }
        void area(int a,int b,int c){
            cout<<"The area of triangle is "<<0.5*a*b<<endl;
        }
        void area(float a){
            cout<<"The area of circle is "<<3.14*r*r<<endl;
        }
};

int main(){
    Area a1;
    a1.getData();
    a1.area(a1.a,a1.b);
    a1.area(a1.a,a1.b,a1.c);
    a1.area(a1.r);

    return 0;

}
