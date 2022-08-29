#include <iostream>
using namespace std;

class Average{
    public:
    static float a;
    static float b;
    static float c;

    static float calculate(){
        return (a+b+c)/3;
    }

    static void print(){
        cout<<"Average is : "<< calculate();
    }

};

float Average::a=5;
float Average::b=6;
float Average::c=7;

int main(){
    Average::print();
}
