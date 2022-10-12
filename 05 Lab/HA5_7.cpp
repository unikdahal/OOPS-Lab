//Extend the program ii. to derive a class 'test' which includes member function to calculate the total marks and percentage of the student. Input the data for a student and display its total marks and percentage/

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

class result : public test
{
public:
    int total;
    float percentage;
    void calculate()
    {
        total = 0;
        for (int i = 0; i < 5; i++)
        {
            total += marks[i];
        }
        percentage = (float)total / 5;
    }
    void display()
    {
        test::display();
        cout << "Total marks of the student: " << total << endl;
        cout << "Percentage of the student: " << percentage << endl;
    }
};

int main()
{
    test t;
    result r;
    r.getdata();
    r.calculate();
    r.display();
    return 0;
}
