// Print the sum, difference and product of two complex numbers by creating a class named 'Complex' with separate functions for each operation whose real and imaginary parts are entered by the user.

#include<iostream>
using namespace std;

class Complex{
    private:
        int a;
        int b;
    public:
        void getData(){
            cout<<"Enter the real part \n";
            cin>>a;
            cout<<"Enter the imaginary part \n";
            cin>>b;

        }
        void Sum(Complex c1,Complex c2){
            a=c1.a+c2.a;
            b=c1.b+c2.b;
        }
        void Difference(Complex c1,Complex c2){
            a=c1.a-c2.a;
            b=c1.b-c2.b;
        }
        void Multiply(Complex c1,Complex c2){
            a=c1.a*c2.a-c1.b*c2.b;
            b=c1.a*c2.a+c1.b*c2.b;
        }
        void Display(){
            cout<<a<<"+"<<"i"<<b<<endl;
        }

};

int main(){
    Complex c1,c2,sum,difference,product;
    c1.getData();
    c2.getData();
    sum.Sum(c1,c2);
    difference.Difference(c1,c2);
    product.Multiply(c1,c2);

    cout<<"The sum is ";
    sum.Display();
    cout<<"The difference is ";
    difference.Display();
    cout<<"The product is ";
    product.Display();




}
