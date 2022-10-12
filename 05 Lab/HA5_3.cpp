// 3. Create two classes which stores distance in feet, inches and meter, centimeter format respectively. Write a function which compares distance in object of these classes and displays the larger one.

#include <iostream>
using namespace std;

class distance2;
class distance1
{
    int feet;
    int inch;
    public:
        void getdata()
        {
            cout<<"Enter the distance in feet and inches: ";
            cin>>feet>>inch;
        }
        friend void compare(distance1, distance2);
};

class distance2
{
    int meter;
    int centimeter;
    public:
        void getdata()
        {
            cout<<"Enter the distance in meter and centimeter: ";
            cin>>meter>>centimeter;
        }
        friend void compare(distance1, distance2);
};

void compare(distance1 d1, distance2 d2)
{
    if((d1.feet * 0.0254) < d2.meter  ){
		cout<<"Distance in meters and centimers is larger\n";
	}
    else if((d1.feet * 0.0254) > d2.meter){
        cout<<"Distance in feet and inches is larger\n";
    }
    else{
        if(d1.inch*2.54 < d2.centimeter){
            cout<<"Distance in meters and centimers is larger\n";
        }
        else if(d1.inch*2.54 > d2.centimeter){
            cout<<"Distance in feet and inches is larger\n";
        }
        else{
            cout<<"Both distances are equal\n";
        }
    }
}

int main()
{
    distance1 d1;
    distance2 d2;
    d1.getdata();
    d2.getdata();
    compare(d1, d2);
    return 0;
}
