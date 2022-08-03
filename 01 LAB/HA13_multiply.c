// 3)Write a function to multiply two values of type int &amp; double and returns the result

#include <stdio.h>
int multiply_int(int a, int b)
{
    return a * b;
}
float multiply_double(float a, float b)
{
    return a * b;
}
int main()
{
    int a, b;
    float c, d;
    printf("Enter two int numbers\n");
    scanf("%d %d", &a, &b);
    printf("The product of two numbers is %d\n", multiply_int(a, b));
    printf("Enter two double numbers\n");
    scanf("%f %f", &c, &d);
    printf("The product of two numbers is %f\n", multiply_double(c, d));
}
