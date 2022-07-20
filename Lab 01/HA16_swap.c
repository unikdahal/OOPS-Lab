// 6) WAP to swap the values of two variables by using a suitable user defined function(say SWAP) for it.

#include <stdio.h>
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
int main()
{
    int a, b;
    printf("Enter two numbers\n");
    scanf("%d %d", &a, &b);
    swap(&a, &b);
    printf("The swapped numbers are %d %d\n", a, b);
    return 0;
}
