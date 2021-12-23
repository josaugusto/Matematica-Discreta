#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int mdc (int a, int mod) {
    int r;
    r = a % mod;
    if (r == 0) {
    return mod;
    }
    return mdc (mod, r);
}
int inverso (int a, int mod, int x) {
    if (mdc (a, mod) != 1) {
        printf ("Infelizmente nao ha um resultado possivel,\npois os valores %d e %d nao sao coprimos!\nCoprimos: dois numeros que possuem apenas o 1 como divisor comum.\n", a, mod);
        return 0;
    }
    if ((a * x) % mod == 1) {
        printf ("O inverso de %d mod %d e %d", a, mod, x);
        return 0;
    }
    return inverso (a, mod, x + 1);
}
int main () {
    int a, mod, x = 0;
    printf ("Digite o valor de A: \n");
    scanf ("%d", &a);
    printf ("Digite o valor de mod: \n");
    scanf ("%d", &mod);
    inverso (a, mod, x);
    return 0;
}