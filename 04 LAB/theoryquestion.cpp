//WAP In C++ to create a class "student " having private data memebrs as student name , age , roll no , and average marrks allocate memory dynamically for storing the name input all the details from keyboard and initialize the object at the time of its creation copy one object instance into another by calling a user defined copy constructor and enter the details of 2 no objects and find out the highest average marks scorer among them using non member function

#include<iostream>
#include<string.h>
using namespace std;

class student{
    private:
        char *name;
        int age;
        int rollno;
        float avgmarks;

    public:
        student(char *n,int a,int r,float m){
            name=new char[strlen(n)+1];
            strcpy(name,n);
            age=a;
            rollno=r;
            avgmarks=m;
        }
        student(student &s){
            name=new char[strlen(s.name)+1];
            strcpy(name,s.name);
            age=s.age;
            rollno=s.rollno;
            avgmarks=s.avgmarks;
        }
        void getdata(){
            cout<<"Enter the name of the student"<<endl;
            cin>>name;
            cout<<"Enter the age of the student"<<endl;
            cin>>age;
            cout<<"Enter the roll no of the student"<<endl;
            cin>>rollno;
            cout<<"Enter the average marks of the student"<<endl;
            cin>>avgmarks;
        }
        void display(){
            cout<<"Name: "<<name<<endl;
            cout<<"Age: "<<age<<endl;
            cout<<"Roll No: "<<rollno<<endl;
            cout<<"Average Marks: "<<avgmarks<<endl;
        }
        friend void highest(student s1,student s2);
};
void highest(student s1,student s2){
    if(s1.avgmarks>s2.avgmarks){
        cout<<"Highest Average Marks Scorer is: "<<endl;
        s1.display();
    }
    else{
        cout<<"Highest Average Marks Scorer is: "<<endl;
        s2.display();
    }
}

int main(){
    student s1.student("Rahul",20,1,90.5);
    student s2(s1);
    s2.getdata();


    highest(s1,s2);
    return 0;
}
