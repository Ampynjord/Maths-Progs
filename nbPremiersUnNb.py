from math import sqrt

print("Trouver les deux nombres premiers qui multipliés donnent un nombre donné")

n = int(input("Entrez un nombre: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_multiplication(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n // i) and n % i == 0:
            return (i, n // i)
    return None

print(prime_multiplication(n))