import sys
import math

input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [False, False] + [True] * (1_000_000 - 1)

# 에라토스테네스의 체를 이용하여 소수를 구함
for i in range(2, int(math.sqrt(1_000_000)) + 1):
    if is_prime[i]:
        for j in range(i * 2, 1_000_000 + 1, i):
            is_prime[j] = False

# 소수를 출력
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
