//WAP to check whether an input integer is perfect number or not.

#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number"<<endl;
    cin>>n;
    int sum=0;
    for(int i=1;i<n;i++){
        if(n%i==0){
            sum=sum+i;
        }
    }
    if(sum==n){
        cout<<"Perfect Number"<<endl;
    }
    else{
        cout<<"Not Perfect Number"<<endl;
    }
    return 0;
}
