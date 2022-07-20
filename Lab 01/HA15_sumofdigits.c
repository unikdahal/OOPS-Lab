// 5) WAP to find out the sum of digits of a number n by using function.

#include <stdio.h>
int sumofdigits(int n)
{
    int sum = 0;
    while (n != 0)
    {
        sum = sum + n % 10;
        n = n / 10;
    }
    return sum;
}
int main()
{
    int n;
    printf("Enter the number\n");
    scanf("%d", &n);
    printf("The sum of digits of %d is %d\n", n, sumofdigits(n));
    return 0;
}
