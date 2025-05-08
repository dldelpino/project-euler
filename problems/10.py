import numpy as np

def summation_of_primes(n): # para programarlo de forma eficiente hay que usar la criba de Eratóstenes
    sum = 0
    i = 2
    primes = (n-1)*[True] # primes[0] -> 2, primes[1] -> 3, ..., primes[n-2] -> n
    while i*i <= n: # si i^2 > n, los múltiplos de i menores que n ya se han tachado
        if primes[i-2] == True:
            for j in range(2, int(n/i)+1):
                primes[i*j-2] = False # i*j está en la posición i*j-2 de la lista
        i += 1
    for i in range(n-1):
        if primes[i] == True:
            sum += i+2 # primes[i] -> i+2
    return sum

print(summation_of_primes(10))
print(summation_of_primes(2000000))