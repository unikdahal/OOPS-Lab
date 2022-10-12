// Create a class which stores account number, customer name and balance. Derive two
// classes from ‘Account’ class: ‘Savings’ and ‘Current’. The ‘Savings’ class stores
// minimum balance. The ‘Current’ class stores the over-due amount. Include member
// functions in the appropriate class for
// -deposit money
// -withdraw [For saving account minimum balance should be checked.]
// [For current account overdue amount should be calculated.]
// -display balance

// From Inheritance including the parameterized constructors in
// all the classes.


#include<iostream>
#include<string.h>
using namespace std;

class Account
{
    int accno;
    char name[20];
public:
    float balance;
    Account(int a,char *n,float b)
    {
        accno=a;
        strcpy(name,n);
        balance=b;
    }
    void deposit(float amt)
    {
        balance+=amt;
    }
    void withdraw(float amt)
    {
        balance-=amt;
    }
    void display()
    {
        cout<<"Account no: "<<accno<<endl;
        cout<<"Name: "<<name<<endl;
        cout<<"Balance: "<<balance<<endl;
    }
};

class Savings:public Account
{
    float minbal;
public:
    Savings(int a,char *n,float b,float m):Account(a,n,b)
    {
        minbal=m;
    }
    void withdraw(float amt)
    {
        if(balance-amt<minbal)
            cout<<"Insufficient balance"<<endl;
        else
            Account::withdraw(amt);
    }
};

class Current:public Account
{
    float od;
public:
    Current(int a,char *n,float b,float o):Account(a,n,b)
    {
        od=o;
    }
    void withdraw(float amt)
    {
        if(balance-amt<od)
            cout<<"Insufficient balance"<<endl;
        else
            Account::withdraw(amt);
    }
};

int main()
{
    Savings s(1,"A",1000,500);
    Current c(2,"B",1000,500);
    s.deposit(1000);
    c.deposit(1000);
    s.withdraw(2000);
    c.withdraw(2000);
    s.display();
    c.display();
    return 0;
}

