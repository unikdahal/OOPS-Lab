//2) Create a class which stores name, roll number and total marks for a student. Input the data for a student and display it.

#include<iostream>
#include<string>
using namespace std;

class student{
    private:
        string name;
        int roll;
        int total;
    public:
        void getdata(){
            cout<<"Enter name: ";
            getline(cin,name);
            cout<<"Enter roll number: ";
            cin>>roll;
            cout<<"Enter total marks: ";
            cin>>total;
        }
        void display(){
            cout<<"Name: "<<name<<endl;
            cout<<"Roll number: "<<roll<<endl;
            cout<<"Total marks: "<<total<<endl;
        }
};

int main(){

    student s;
    s.getdata();
    s.display();
    return 0;

}
