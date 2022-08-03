//iii. Modify the program ii) to store marks in 5 subjects. Calculate the total marks andb percentage of a student and display it.

#include<iostream>
#include<string>
using namespace std;

class student{
    private:
        string name;
        int roll;
        int total;
        int marks[5];
    public:
        void getdata(){
            cout<<"Enter name: ";
            getline(cin,name);
            cout<<"Enter roll number: ";
            cin>>roll;
            for(int i=0;i<5;i++){
                cout<<"Enter marks of subject "<<i+1<<": ";
                cin>>marks[i];
            }
        }
        void display(){
            cout<<"Name: "<<name<<endl;
            cout<<"Roll number: "<<roll<<endl;
            for(int i=0;i<5;i++){
                total=total+marks[i];
            }
            cout<<"Total marks: "<<total<<endl;
            cout<<"Percentage: "<<(total/5)<<"%"<<endl;
        }

};

int main(){

    student s;
    s.getdata();
    s.display();
    return 0;

}
