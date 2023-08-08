import math


def getPrimes(n):
    is_prime = [False, False] + [True] * (n - 1)
    max_len = int(math.sqrt(n))

    for i in range(2, max_len):
        if is_prime[i]:
            for j in range(2 * i, n, i):
                is_prime[j] = False

    return [i for i in range(2, n) if is_prime[i]]


list_primes = getPrimes(100000)
set_primes = set(list_primes)

N = int(input())

for _ in range(N):
    num = int(input())
    ans = 0

    while ans == 0:
        if not num in set_primes:
            for p in list_primes:
                div = num // p
                if num % p == 0 and (div in set_primes) and (div != p):
                    ans = num
                    break
        num += 1
    print(ans)
