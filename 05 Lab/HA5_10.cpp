// 10. Create a class which stores emplouee name, id and salary. Derive two classes from 'Employee' class: 'Regular' and 'Part-Time'. The 'Regular' class stores DA, HRA and basic salary. The 'Part-Time' class stores the number of hours and pay per hour. Calculate the salary of a regular employee and a part-time employee.

#include <iostream>
using namespace std;

class Employee
{
public:
    char name[20];
    int id;
    int salary;
};

class Regular : public Employee
{
public:
    int DA;
    int HRA;
    int basic;
    int total;
    void getdata()
    {
        cout << "Enter the name of the employee: ";
        cin >> name;
        cout << "Enter the id of the employee: ";
        cin >> id;
        cout << "Enter the salary of the employee: ";
        cin >> salary;
        cout << "Enter the DA of the employee: ";
        cin >> DA;
        cout << "Enter the HRA of the employee: ";
        cin >> HRA;
        cout << "Enter the basic salary of the employee: ";
        cin >> basic;
        total=salary+DA+HRA+basic;
    }
    void display()
    {
        cout << "Name of the employee: " << name << endl;
        cout << "Id of the employee: " << id << endl;
        cout << "Salary of the employee: " << salary << endl;
        cout << "DA of the employee: " << DA << endl;
        cout << "HRA of the employee: " << HRA << endl;
        cout << "Basic salary of the employee: " << basic << endl;
        cout << "Total salary of the employee: " << total << endl;
    }
};

class PartTime : public Employee
{

public:
    int hours;
    int pay;
    int total;
    void getdata()
    {
        cout << "Enter the name of the employee: ";
        cin >> name;
        cout << "Enter the id of the employee: ";
        cin >> id;
        cout << "Enter the salary of the employee: ";
        cin >> salary;
        cout << "Enter the number of hours of the employee: ";
        cin >> hours;
        cout << "Enter the pay per hour of the employee: ";
        cin >> pay;
        total=salary+(hours*pay);
    }
    void display()
    {
        cout << "Name of the employee: " << name << endl;
        cout << "Id of the employee: " << id << endl;
        cout << "Salary of the employee: " << salary << endl;
        cout << "Number of hours of the employee: " << hours << endl;
        cout << "Pay per hour of the employee: " << pay << endl;
        cout << "Total salary of the employee: " << total << endl;
    }
};

int main()
{
    Regular r;
    PartTime p;
    cout<<"Regular employee details: "<<endl;
    r.getdata();
    cout<<"Part time employee details: "<<endl;
    p.getdata();
    r.display();
    p.display();
    return 0;
}
