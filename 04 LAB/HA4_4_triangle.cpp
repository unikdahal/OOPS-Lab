#include<iostream>
using namespace std;

class Triangle
{

    private:
        float l,b,h;
    public:
        void get_data(){
            cout<<"Enter the length \n";
            cin>>l;
            cout<<"Enter the breadth \n";
            cin>>b;
            cout<<"Enter the height \n";
            cin>>h;
        }
        float area(){
            return 0.5*b*h;
        }
        float perimeter(){
            return l+b+h;
        }
};

int main(){


    Triangle t1;
    t1.get_data();
    cout<<"Area is "<<t1.area()<<"\n"<<"Perimeter is \n"<<t1.perimeter()<<endl;


}
