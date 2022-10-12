// Write C++ Program to display the cube of the number upto a given integer using friend function.

#include<iostream>
using namespace std;

class cube{
    int n;
    public:
        void getdata(){
            cout<<"Enter the number: ";
            cin>>n;
        }
        friend void display(cube);
};

void display(cube c){
    for(int i=1;i<=c.n;i++){
        cout<<i*i*i<<endl;
    }
}

int main(){
    cube c;
    c.getdata();
    display(c);
    return 0;
}
