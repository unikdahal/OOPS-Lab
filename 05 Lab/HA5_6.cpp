//Create a class student which stores name, roll number and age of a student . Derive a class test from student class which stores marks in 5 subjects Input and Display the details of the student

#include <iostream>
using namespace std;

class student
{
public:
    char name[20];
    int roll;
    int age;
};

class test : public student
{
public:
    int marks[5];
    void getdata()
    {
        cout << "Enter the name of the student: ";
        cin >> name;
        cout << "Enter the roll number of the student: ";
        cin >> roll;
        cout << "Enter the age of the student: ";
        cin >> age;
        cout << "Enter the marks of the student: ";
        for (int i = 0; i < 5; i++)
        {
            cin >> marks[i];
        }
    }
    void display()
    {
        cout << "Name of the student: " << name << endl;
        cout << "Roll number of the student: " << roll << endl;
        cout << "Age of the student: " << age << endl;
        cout << "Marks of the student: ";
        for (int i = 0; i < 5; i++)
        {
            cout << marks[i] << " ";
        }
        cout << endl;
    }
};

int main()
{
    test t;
    t.getdata();
    t.display();
    return 0;
}
