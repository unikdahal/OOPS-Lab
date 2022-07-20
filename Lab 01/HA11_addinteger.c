// 1)Write a function to add two values of type integer and returns the result

#include <stdio.h>
int add(int a, int b)
{
    return a + b;
}
int main()
{
    int a, b;
    printf("Enter two numbers\n");
    scanf("%d %d", &a, &b);
    printf("The sum of two numbers is %d\n", add(a, b));
    return 0;
}
