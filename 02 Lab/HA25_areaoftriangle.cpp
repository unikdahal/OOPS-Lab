//WAP to calculate the area of a triangle using Heron’s Formula.

#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int a,b,c;
    cout<<"Enter the length of the sides of the triangle"<<endl;
    cin>>a>>b>>c;
    int s=(a+b+c)/2;
    float area=sqrt(s*(s-a)*(s-b)*(s-c));
    cout<<"The area of the triangle is "<<area<<endl;
    return 0;
}
