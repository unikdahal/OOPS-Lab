//Write a program to print the area of a rectangle by creating a class named 'Area' having two functions. First function named as 'setDim' takes the length and breadth of the rectangle as parameters and the second function named as 'getArea' returns the area of the rectangle. Length and breadth of the rectangle are entered through keyboard.

#include<iostream>
using namespace std;

class Area
{

    private:
        float l,b;
    public:
        void setDim(){
            cout<<"Enter the length \n"<<endl;
            cin>>l;
            cout<<"Enter the breadth \n"<<endl;
            cin>>b;
        }
        float getArea(){
            return l*b;
        }
};

int main(){


    Area r1;
    r1.setDim();
    cout<<"Area is "<<r1.getArea()<<"\n";

    return 0;
}
