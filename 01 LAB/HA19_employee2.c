//9)Write a program to read the name, address,and salary of 5 employees using array of structure .Display information of each employee in alphabetical order of their name.

#include<stdio.h>
#include<string.h>

struct employee{
    char name[20];
    char address[20];
    int salary;
};
int main(){;
    struct employee a[5];
    for (int i = 0; i < 5; i++)
    {
        printf("Enter the name address and salary of the employee\n");
        scanf("%s %s %d",a[i].name,a[i].address,&a[i].salary);
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = i+1; j < 5; j++)
        {
            if(strcmp(a[i].name,a[j].name)>0){
                struct employee temp;
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%s %s %d\n",a[i].name,a[i].address,a[i].salary);
    }
    return 0;
}
