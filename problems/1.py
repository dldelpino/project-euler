multiples = []
for n in range(1, 1000):
    if n % 3 == 0:
        multiples.append(n)
    elif n % 5 == 0:
        multiples.append(n)

print(sum(multiples))