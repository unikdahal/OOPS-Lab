// 7) WAP to test whether a number n is palindrome number or not.

#include <stdio.h>

int isPalindrome(int n)
{
    int temp = n;
    int rev = 0;
    while (n != 0)
    {
        rev = rev * 10 + n % 10;
        n = n / 10;
    }
    if (temp == rev)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main()
{
    int n;
    printf("Enter the number\n");
    scanf("%d", &n);
    if (isPalindrome(n) == 1)
    {
        printf("%d is a palindrome number\n", n);
    }
    else
    {
        printf("%d is not a palindrome number\n", n);
    }
    return 0;
}
