def mdc (a, mod): #Calcular o MDC
    r = a % mod 
    if (r == 0):
        return mod
    return mdc(mod, r)
 
def inverso (a, mod, x): #Calcular o inverso de a mod m
    if (mdc(a, mod) != 1):
        return mdc(a, mod)
 
    if ((a * x) % mod == 1):
        return x
 
    return inverso (a, mod, x + 1)
 
def congruencia (a, b, mod):
    x = 0
    a_barra = inverso(a, mod, x)
    d = mdc(a, mod)
 
    if (d == 1): #São coprimos, portanto existe solução única
        res = b * a_barra #Resultado de X
 
        if (res > mod):
            res = res % mod
 
        print(f"Existe uma solução única entre 0 e {mod}, essa solução é: {res}")
    else: #Não são coprimos, então é necessário verificar se existe e quantas soluções existe
        if (b % d == 0): #Existe d soluções
            #Transformando em solução única
            a /= d
            b /= d
            mod /= d
 
            #Encontrando a solução única
            a_barra = inverso(a, mod, x)
            res = b * a_barra
 
            if (res > mod):
                res = res % mod
 
            print(f"Existem {d} soluções, são elas: ")
            for solucoes in range(0, d):
                print(int(res + mod * solucoes))
        else:
            print("Não existe solução!\n")
 
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
mod = int(input("Digite o valor do mod: "))
 
congruencia(a, b , mod)