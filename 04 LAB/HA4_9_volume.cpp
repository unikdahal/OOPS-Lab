// C++ program to find volume of cube, cylinder, sphere by function overloading

#include<iostream>
using namespace std;

class Volume{
    public:
        int l;
        int r;
        void getData(){
            cout<<"Enter the length \n";
            cin>>l;
            cout<<"Enter the radius \n";
            cin>>r;
        }
        void volume(int l){
            cout<<"The volume of cube is "<<l*l*l<<endl;
        }
        void volume(int l,int r,float pi){
            cout<<"The volume of cylinder is "<<pi*r*r*l<<endl;
        }
        void volume(float r,float pi){
            cout<<"The volume of sphere is "<<1.33*pi*r*r*r<<endl;
        }
};

int main(){
    Volume v1;
    v1.getData();
    v1.volume(v1.l);
    v1.volume(v1.l,v1.r,3.14);
    v1.volume(v1.r,3.14);

    return 0;

}
