import os
from threading import Timer
from math import sqrt
import time
 
def exitfunc():
    os._exit(0)
 
def primos(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
 
start_time = time.time()
Timer(60, exitfunc).start()
 
print(primos(200000000))