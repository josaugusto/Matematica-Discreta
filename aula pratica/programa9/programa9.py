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
 
        #print(f"Existe uma solução única entre 0 e {mod}, essa solução é: {res}")
        return res
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
 
qnts_congruencias = 3
list_a = []
list_b = []
list_mod = []
while (qnts_congruencias > 0):
    a = int(input("Digite o valor de a: "))
    list_a.append(a)
    b = int(input("Digite o valor de b: "))
    list_b.append(b)
    mod = int(input("Digite o valor do Mod: "))
    list_mod.append(mod)
    print("=-" * 15)
    qnts_congruencias -= 1
 
#Checar se os módulos são coprimos
list_mod1 = list_mod
list_mdc = []
for i in list_mod:
    for j in list_mod1:
        if(i != j):
            if(mdc(i, j) == 1):
                list_mdc.append(1)
            else:
                list_mdc.append(2)
 
coprimos = len(set(list_mdc))
if (coprimos == 1):
    #Calcular o M
    m = 0
    for mod in range(0, len(list_mod)):
        if (mod == 0):
            m += list_mod[mod]
        else:
            m *= list_mod[mod]
 
    x0 = 0
    for mod in range(0, len(list_mod)):
        m1 = m / list_mod[mod]
        s1 = congruencia(m1, 1, list_mod[mod])
        x0 += int(m1) * int(s1) * int(list_b[mod])
 
    if (x0 > m):
        x0 = x0 % m
    print(x0)
else:
    print("Os módulos não são coprimos!")
 