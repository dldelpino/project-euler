def sum_square_difference(n):
    naturals = []
    for i in range(1, n+1):
        naturals.append(i)
    x = sum(naturals)**2
    y = sum([n**2 for n in naturals])
    z = x - y
    return z

print(sum_square_difference(10))
print(sum_square_difference(100))