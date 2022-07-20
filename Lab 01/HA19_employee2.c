//9)Write a program to read the name, address,and salary of 5 employees using array of structure .Display information of each employee in alphabetical order of their name.

#include<stdio.h>

struct employee{
    char name[20];
    char address[20];
    int salary;
};



int main(){
    struct employee a[5];

    for (int i = 0; i < 5; i++)
    {
        printf("Enter the name address age and salary of the employee");
        scanf("%s %s %d",a[i].name,a[i].address,&a[i].salary);
    }
}
