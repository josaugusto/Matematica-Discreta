numero = int(input("Digite um número (n>1): "))
fatores = []
divisor = 2
print(f"{numero} = ", end='')
 
while (numero > 1):
    if (numero % divisor == 0):
        fatores.append(divisor)
        numero /= divisor
    else:
        divisor += 1
 
 
if (len(fatores) == 1):
    print(fatores[0])
else:
    i = 0
    while (i < len(fatores)):
        print(f"{fatores[i]} * ", end='')
        i += 1
        if (i == len(fatores) - 1):
            print(f"{fatores[i]}")
            break