import numpy as np
from math import sqrt
from sympy import sieve
import threading
from tqdm import tqdm

def sieve_of_eratosthenes(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0:2] = False

    for i in range(2, int(sqrt(n))+1):
        if is_prime[i]:
            is_prime[i*i::i] = False

    primes = set(np.where(is_prime)[0][2:])
    return primes

def find_prime_product(start, end, progress_bar, primes):
    for x in range(start, end):
        for y in range(1, x+1):
            product = x * y
            if product in primes:
                if x == 1 and y in primes:
                    continue
                progress_bar.update(1)

def find_prime_product_multithreaded(num_threads):
    max_value = int(input("Entrez la valeur maximale : "))
    primes = set(sieve.primerange(2, max_value))  # Utiliser la fonction primerange de la bibliothèque sympy

    chunk_size = max_value // num_threads
    threads = []

    total_iterations = chunk_size * num_threads
    with tqdm(total=total_iterations, unit='iterations', desc='Progress') as pbar:
        for i in range(num_threads):
            start = i * chunk_size + 1
            end = (i + 1) * chunk_size + 1
            thread = threading.Thread(target=find_prime_product, args=(start, end, pbar, primes))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

num_threads = 4
find_prime_product_multithreaded(num_threads)
