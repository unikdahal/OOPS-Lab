//9.WAP to check whether a number n is prime number or not.

#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number"<<endl;
    cin>>n;
    int prime=0;
    for(int i=2;i<=n/2;i++){
        if(n%i==0){
            prime=1;
            break;
        }
    }
    if(prime==0){
        cout<<"Prime"<<endl;
    }
    else{
        cout<<"Not Prime"<<endl;
    }
    return 0;
}
