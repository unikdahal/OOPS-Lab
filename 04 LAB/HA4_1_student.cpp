//Create a class named 'Student' with a string variable 'name' and an integer variable 'roll_no'. Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.

#include<iostream>
using namespace std;

class Student{

    private:
        string name;
        int rollno;
    public:
        void getData(){
            name="John";
            rollno=2;
        }
        void display(){
            cout<<name<<" "<<rollno<<endl;
        }


};
int main(){

    Student s1;
    s1.getData();
    s1.display();

}
