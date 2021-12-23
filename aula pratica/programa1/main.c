#include <stdio.h>


int eh_primo(int n, int contador, int divisor)
{
    if (contador > 2 || n == 1 || n == 0) return 0;
    if (n%divisor == 0 && divisor <= n) eh_primo(n, contador+=1, divisor+=1);
    else if (n%divisor != 0 && divisor <= n) eh_primo(n, contador, divisor+=1);
    else return 1;
}

int main()
{
    int num = 0;
    printf("Numero: "); scanf("%d", &num);

    if (eh_primo(num, 0, 1)) printf("O numero %d É primo\n", num);
    else printf("O numero %d NÃO é primo\n", num);
    
    return 0;
}