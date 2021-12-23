def eh_primo(num, contador, divisor):

    if (contador > 2 or num == 1 or num == 0): return False
    elif (num%divisor == 0 and divisor <= num): return eh_primo(num, contador+1, divisor+1)
    elif (num%divisor != 0 and divisor <= num): return eh_primo(num, contador, divisor+1)
    else: return True

def proximo_primo(num):

    if eh_primo(num, 0, 1): return num
    return proximo_primo(num+1)

def mdc(num1, num2):

    if (num1 > num2 and num1%num2 == 0):
        return num2
    else:
        return mdc(num2, num1%num2)

    if (num2 > num1 and num2%num1 == 0):
        return num1
    else:
        return mdc(num1, num2%num1)

def mmc(num1, num2, divisor, resultado):

    if num1 == 1 and num2 == 1:
        return resultado
    elif num1%divisor == 0 and num2%divisor == 0:
        return mmc(num1/divisor, num2/divisor, divisor, divisor*resultado)
    elif num1%divisor == 0 and not(num2%divisor == 0):
        return mmc(num1/divisor, num2, divisor, divisor*resultado)
    elif not(num1%divisor == 0) and num2%divisor == 0:
        return mmc(num1, num2/divisor, divisor, divisor*resultado)
    else:
        return mmc(num1, num2, proximo_primo(divisor+1), resultado)


num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

print(f"MDC({num1}, {num2}) = {mdc(num1, num2)}")
print(f"MMC({num1}, {num2}) = {mmc(num1, num2, 2, 1)}")
