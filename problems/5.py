import math

def smallest_multiple(n): # menor número natural que es divisible por todos los números de 1 a n
    factors = []
    for i in range(1, n+1):
        j = i
        for f in factors:
            if j % f == 0:
                j = int(j/f)
        if j > 1:
            factors.append(j)
    sol = math.prod(factors) # multiplicar los elementos de una lista
    return sol
    
print(smallest_multiple(10))
print(smallest_multiple(20))