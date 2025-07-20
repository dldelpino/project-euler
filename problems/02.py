sum = 0
f0 = 1
f1 = 2
while f1 <= 4e6:
    if f1 % 2 == 0:
        sum += f1
    aux = f1
    f1 += f0
    f0 = aux

print(sum)