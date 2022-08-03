// Create a class distance which stores a distance in feet and inches. Input 2 distance values in objects, add them, store the resultant distance in and object and display it.
// a) store the resultant distance in the calling object:C3.add(C1,C2)

#include <iostream>
using namespace std;

class Calculate{
    public:
    int feet;
    int inches;
    int result;

    void takeInput(){
        cout<<"Enter distance: "<<endl;
        cout<<"In feet: ";
        cin>>feet;
        cout<<"In inches: ";
        cin>>inches;
    }

    void calc(Calculate x, Calculate y){
        feet = x.feet + y.feet;
        inches = x.inches + y.inches;
        if(inches>=12){
            feet++;
            inches-=12;
        }
    }

    void display(){
        cout<<"The sum is: "<<feet<<"feet "<<inches<<"inch"<<endl;
    }
};
int main(){
    Calculate a,b,c;
    a.takeInput();
    b.takeInput();
    c.calc(a,b);
    c.display();
}
