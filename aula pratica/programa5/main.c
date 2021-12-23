#include <stdio.h>

int mdc(int n1, int n2)
{
    if (n1 > n2 && n1%n2 == 0) return n2;
    else return mdc(n2, n1%n2);
    if (n2 > n1 && n2%n1 == 0) return n1;
    else return mdc(n1, n2%n1);
}

int main()
{
    int num1, num2 = 0;

    printf("Número 1: "); scanf("%d", &num1);
    printf("Número 2: "); scanf("%d", &num2);

    printf("MDC(%d, %d) = %d\n", num1, num2, mdc(num1, num2));
    
    return 0;
}