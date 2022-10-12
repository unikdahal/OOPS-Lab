// Create a class student which stores name, roll number and age of a student. Derive a class
// test from student class, which stores marks in 5 subjects. Input and display the details of
// a student.
//Extend the program ii. of inheritance to include a class sports, which stores the marks in
// sports activity. Derive the result class from the classes ‘test’ and ‘sports’. Create objects
// using parameterized constructors .Calculate the total marks and percentage of a student.

#include<iostream>
#include<string.h>
using namespace std;


class student
{
    char name[20];
    int roll;
    int age;
public:

    student(char *n,int r,int a)
    {
        strcpy(name,n);
        roll=r;
        age=a;
    }
    void display()
    {
        cout<<"Name: "<<name<<endl;
        cout<<"Roll: "<<roll<<endl;
        cout<<"Age: "<<age<<endl;
    }
};

class test:public student
{
    int marks[5];
public:
    test(char *n,int r,int a,int m[]):student(n,r,a)
    {
        for(int i=0;i<5;i++)
            marks[i]=m[i];
    }
    void display()
    {
        student::display();
        cout<<"Marks: ";
        for(int i=0;i<5;i++)
            cout<<marks[i]<<" ";
        cout<<endl;
    }
};

class sports
{
    int marks;
public:
    sports(int m)
    {
        marks=m;
    }
    void display()
    {
        cout<<"Sports Marks: "<<marks<<endl;
    }
};

class result:public test,public sports
{
    int total;
    float percentage;
public:
    result(char *n,int r,int a,int m[],int s):test(n,r,a,m),sports(s)
    {
        total=0;
        for(int i=0;i<5;i++)
            total+=m[i];
        total+=s;
        percentage=total/6.0;
    }
    void display()
    {
        test::display();
        sports::display();
        cout<<"Total: "<<total<<endl;
        cout<<"Percentage: "<<percentage<<endl;
    }
};

int main()
{
    int m[5]={10,20,30,40,50};
    result r("ABC",1,20,m,60);
    r.display();
    return 0;
}
