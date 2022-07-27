//Program to find average marks obtained by a class of 10 students in a test.

#include<iostream>
using namespace std;

int main(){
    float marks[10];
    float sum=0;
    for(int i=0;i<10;i++){
        cout<<"Enter the marks of student "<<i+1<<endl;
        cin>>marks[i];
        sum=sum+marks[i];
    }
    float average=sum/10;
    cout<<"The average marks of the class is "<<average<<endl;
    return 0;
}
