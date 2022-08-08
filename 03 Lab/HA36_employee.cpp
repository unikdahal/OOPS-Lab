// Create a class which stores id, name, age and basic salary of an employee. Input data for
// n number of employees. Calculate the gross salary of all the employees and display it
// along with all other details in a tabular form.
// [Gross salary= Basic salary + DA + HRA,
// DA = 80% of Basic salary
// HRA=10% of Basic salary ]

#include<iostream>
#include<string.h>
using namespace std;

class employee{
    private:
        int id;
        string name;
        int age;
        int basic;
    public:
        void getdata(){
            cout<<"Enter id: ";
            cin>>id;
            cout<<"Enter name: ";
            cin.ignore();
            getline(cin,name);
            cout<<"Enter age: ";
            cin>>age;
            cout<<"Enter basic salary: ";
            cin>>basic;
        }
        void display(){
            cout<<id<<" \t "<<name<<" \t "<<age<<"\t "<<basic<<"\t\t "<<basic+(basic*0.8)+basic*0.1<<endl;
        }
};

int main(){
    int n;
    cout<<"Enter number of employees: ";
    cin>>n;
    employee e[n];
    for(int i=0;i<n;i++){
        e[i].getdata();
    }
    cout<<endl<<"Id\t Name\t Age\t Basic Salary\t Gross Salary"<<endl;

    for(int i=0;i<n;i++){
        e[i].display();
    }
    return 0;
}
