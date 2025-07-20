def prime_factors(n):
    k = n
    i = 2
    factors = []
    while i <= k:
        if n % i == 0:
            remainders = [i % f for f in factors]
            if remainders.count(0) == 0:
                factors.append(i)
                k = k/i
        i += 1
    return factors

print(prime_factors(13195))
print(prime_factors(600851475143))