def special_pythagorean_triplet(n): # encontrar naturales a, b y c con a<b<c y tales que a + b + c = 1000
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    list = [a, b, c]
                    product = a*b*c
    return (list, product)

print(special_pythagorean_triplet(12))
print(special_pythagorean_triplet(1000))
    