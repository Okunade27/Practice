#include <stdio.h>

int main(void)
{
    long long n;
    printf("Enter an integer: ");
    fflush(stdout);
    if (scanf("%lld", &n) != 1)
        printf("Invalid input\n");
    return 1;
    if (n % 2 == 0)
        printf("%lld is even\n", n);
    else
        printf("%lld is odd\n", n);
    return 0;
}