//WAP to calculate the sum of digits of a given number.

#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number"<<endl;
    cin>>n;
    int sum=0;
    while(n!=0){
        sum=sum+n%10;
        n=n/10;
    }
    cout<<"The sum of digits is "<<sum<<endl;
    return 0;
}
