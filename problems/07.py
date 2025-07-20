def nth_prime(n): # devuelve el n-ésimo número primo
    primes = []
    m = len(primes)
    i = 2
    while m < n:
        j = 0
        k = 0
        while j < m and k == 0:
            p = primes[j]
            if i % p == 0:
                k = 1
            j += 1
        if k == 0:
            primes.append(i)
        i += 1
        m = len(primes)
    sol = primes[-1]
    return sol

print(nth_prime(6))
print(nth_prime(10001)) # tarda un poco... seguramente se pueda optimizar el programa
