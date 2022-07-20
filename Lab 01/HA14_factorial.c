// 4)WAP to find the factorial of a number n by using a suitable user defined function(say fact) for it.

#include <stdio.h>
int fact(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return n * fact(n - 1);
    }
}
int main()
{
    int n;
    printf("Enter the number\n");
    scanf("%d", &n);
    printf("The factorial of %d is %d\n", n, fact(n));
    return 0;
}
