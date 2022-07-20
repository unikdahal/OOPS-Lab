//8) Define a structure of employee having data members name, address, age and salary.Take the data for n employees in an array and find the average salary.

#include<stdio.h>

struct employee{
    char name[20];
    char address[20];
    int age;
    int salary;
};

int avgsalary(struct employee a[],int n){
    int total=0;
    for(int i=0;i<n;i++){
        total+=a[i].salary;
    }
    return total/n;
}
int main(){
    int n;
    printf("How many employee data you would like to store?");
    scanf("%d",&n);
    struct employee a[n];

    for (int i = 0; i < n; i++)
    {
        printf("Enter the name address age and salary of the employee");
        scanf("%s %s %d %d",a[i].name,a[i].address,&a[i].age,&a[i].salary);
    }
    int avg=avgsalary(a,n);
    printf("The average salary is %d",avg);
    return 0;
}
