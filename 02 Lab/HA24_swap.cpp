#include<iostream>
using namespace std;

void callByValue(int x,int y){
    int temp=x;
    x=y;
    y=temp;

    cout<<"Swapping using call by Value The value of x and y are "<<x<<y<<endl;
}

int main(){
    int a,b;
    cin>>a,b;

    callByValue()
}
