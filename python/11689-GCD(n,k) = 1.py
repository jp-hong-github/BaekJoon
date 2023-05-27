import sys

input = sys.stdin.readline


def euler_phi(number):
    result = number
    p = 2
    while p * p <= number:
        if number % p == 0:
            while number % p == 0:
                number //= p
            result -= result // p
        p += 1
    if number > 1:
        result -= result // number
    return result


n = int(input())
result = euler_phi(n)
print(result)
