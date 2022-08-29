#include<iostream>
using namespace std;

class student{
    public:
    int rollno;
    double marks;
    void getdata();
    void display();
};

void student::getdata(){
    cout<<"Enter roll no"<<endl;
    cin>>rollno;
    cout<<"Enter marks"<<endl;
    cin>>marks;

}
void student::display(){
    cout<<rollno<<" "<<marks<<endl;

}
int main(){
    int i;
    student st[4];
    for(int i=0;i<5;i++){
        st[i].getdata();
    }
    for(int i=0;i<5;i++){
        st[i].display();
    }
}
