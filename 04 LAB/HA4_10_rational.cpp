//C++ class Program to perform rational number arithmetic

#include<iostream>
using namespace std;

class Rational{
    private:
        int num;
        int den;
    public:
        void getData(){
            cout<<"Enter the numerator \n";
            cin>>num;
            cout<<"Enter the denominator \n";
            cin>>den;
        }
        void Sum(Rational r1,Rational r2){
            int num1=r1.num*r2.den+r2.num*r1.den;
            int den1=r1.den*r2.den;
            cout<<"The sum is "<<num1<<"/"<<den1<<endl;
        }
        void Difference(Rational r1,Rational r2){
            int num1=r1.num*r2.den-r2.num*r1.den;
            int den1=r1.den*r2.den;
            cout<<"The difference is "<<num1<<"/"<<den1<<endl;
        }
        void Product(Rational r1,Rational r2){
            int num1=r1.num*r2.num;
            int den1=r1.den*r2.den;
            cout<<"The product is "<<num1<<"/"<<den1<<endl;
        }
        void divide(Rational r1,Rational r2){
            int num1=r1.num*r2.den;
            int den1=r1.den*r2.num;
            cout<<"The quotient is "<<num1<<"/"<<den1<<endl;
        }
};
int main(){
    Rational r1,r2;
    r1.getData();
    r2.getData();
    r1.Sum(r1,r2);
    r1.Difference(r1,r2);
    r1.Product(r1,r2);
    r1.divide(r1,r2);

    return 0;
}
