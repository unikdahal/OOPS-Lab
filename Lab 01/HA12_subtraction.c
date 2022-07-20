// 2)Write a function to subtract two values of type float and returns the result

#include <stdio.h>
float sub(float a, float b)
{
    return a - b;
}
int main()
{
    float a, b;
    printf("Enter two numbers\n");
    scanf("%f %f", &a, &b);
    printf("The difference of two numbers is %f\n", sub(a, b));
    return 0;
}
