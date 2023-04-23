import sys

input = sys.stdin.readline
a, b = map(int, input().split())
if b > 10000000:
    b = 10000000


def check_prime(number):
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


for i in range(a, b + 1):
    if str(i) == str(i)[::-1] and check_prime(i):
        print(i)

print(-1)
