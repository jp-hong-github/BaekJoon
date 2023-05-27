import random
import sys


input = sys.stdin.readline


def miller_rabin(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    if n < 2047:
        k = 1
    elif n < 1373653:
        k = 2
    elif n < 25326001:
        k = 3
    elif n < 3215031751:
        k = 4
    elif n < 2152302898747:
        k = 5
    elif n < 3474749660383:
        k = 6
    elif n < 341550071728321:
        k = 7
    else:
        k = 8

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
