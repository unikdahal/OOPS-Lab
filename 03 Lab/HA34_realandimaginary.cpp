// Create a class complex which stores real and imaginary part of a complex number. Input 10 complex numbers and display them.

#include<iostream>
#include<string>
using namespace std;

class complex{
    private:
        int real[10];
        int imag[10];
    public:
        void getdata(){
            for(int i=0;i<10;i++){
                cout<<"Enter real part of complex number "<<i+1<<": ";
                cin>>real[i];
                cout<<"Enter imaginary part of complex number "<<i+1<<": ";
                cin>>imag[i];
            }
        }
        void display(){
            for(int i=0;i<10;i++){
                cout<<"Complex number "<<i+1<<": "<<real[i]<<" + "<<"i"<<imag[i]<<endl;
            }
        }

};

int main(){

        complex c;
        c.getdata();
        c.display();
        return 0;

}
