//WAP to find the first n numbers of a Fibonacci sequence

#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number"<<endl;
    cin>>n;
    int a=0,b=1,c;
    cout<<a<<" "<<b<<" ";
    for(int i=0;i<n-2;i++){
        c=a+b;
        a=b;
        b=c;
        cout<<c<<" ";
    }
    return 0;
}
