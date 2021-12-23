def mdc(a, b):
    quocientes = []
    if (a < b):
        temp = b
        b = a
        a = temp
 
    r = a % b
    quocientes.append(a//b)
    while (r != 0):
        a = b
        b = r
        r = a % b
        quocientes.append(a//b)
    return quocientes
 
def euclides(a, b):
    if (a % b == 0):
        return b
 
    return euclides(b, a%b)
 
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
mdc = mdc(n1, n2)
del mdc[-1]
mdc = list(reversed(mdc))
 
x = 0
c = 1
fatores = []
if(len(mdc) == 1):
    fatores.append(-1)
    v = 1
 
for quociente in mdc:
    r = quociente * c + x
    fatores.append(r)
    temp = c
    c = r
    x = temp
if (len(fatores) % 2 == 0):
    s = fatores[-2] * -1
    t = fatores[-1]
else:
    s = fatores[-2]
    t = fatores[-1] * -1
 
if(v == 1):
    t *= -1
print(f"Os coeficientes lineares são: {s} e {t}")
eucli = euclides(n1, n2)
if (n2 > n1):
    temp = n1
    n1 = n2
    n2 = temp
print(f"{eucli} = {s} * {n1} + {t} * {n2}")