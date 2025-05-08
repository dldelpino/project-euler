def is_palindrome(n):
    var = False
    if str(n) == str(n)[::-1]: # str(n)[::-1] es str(n) dado la vuelta
        var = True
    return var

def largest_palindrome(n): # palíndromo más grande como producto de números de n cifras
    i = pow(10, n-1)
    j = pow(10, n)
    palindrome = 0
    while i < j:
        for k in range(i, j):
            l = i*k
            if is_palindrome(l) and l > palindrome:
                palindrome = l
        i += 1
    return palindrome

print(largest_palindrome(2))
print(largest_palindrome(3)) 
# para n = 4 tarda unos 30 segundos, y sale 99000099