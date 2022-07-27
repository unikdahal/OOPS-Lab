//WAP to find the GCD/HCF of two numbers .

#include<iostream>
using namespace std;

int main(){
    int a,b;
    cout<<"Enter the two numbers"<<endl;
    cin>>a>>b;
    int gcd=1;
    for(int i=1;i<=a&&i<=b;i++){
        if(a%i==0&&b%i==0){
            gcd=i;
        }
    }
    cout<<"The GCD is "<<gcd<<endl;
    return 0;
}
