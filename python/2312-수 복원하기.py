import sys
import math
from collections import defaultdict

input = sys.stdin.readline


def prime_factorization(number):
    factors = defaultdict(int)
    while number % 2 == 0:
        factors[2] += 1
        number //= 2

    sqrt = int(math.sqrt(number)) + 1
    for i in range(3, sqrt, 2):
        while number % i == 0:
            factors[i] += 1
            number //= i

    if number > 2:
        factors[number] += 1

    return factors


T = int(input())
for _ in range(T):
    N = int(input())
    factors = prime_factorization(N)
    factors = sorted(factors.items(), key=lambda x: x[0])
    for factor, count in factors:
        print(factor, count)
