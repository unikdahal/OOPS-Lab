// Write a C++ Program to display the reverse of a number using the Friend function

#include<iostream>
using namespace std;

class reverse{
    int n;
    public:
        void getdata(){
            cout<<"Enter the number: ";
            cin>>n;
        }
        friend void display(reverse);
};

void display(reverse r){
    int rev=0;
    while(r.n!=0){
        rev=rev*10+r.n%10;
        r.n/=10;
    }
    cout<<"Reverse of the number is: "<<rev<<endl;
}

int main(){
    reverse r;
    r.getdata();
    display(r);
    return 0;
}

