import sys

input = sys.stdin.readline

n = int(input())

# 에라토스테네의 체
sieve = [False, False] + [True for _ in range(n - 1)]

for i in range(2, n // 2 + 1):
    if sieve[i] == True:
        for j in range(2 * i, n + 1, i):
            sieve[j] = False

primes: list = [idx for idx in range(2, n + 1) if sieve[idx]]

# n=4000000일 경우 283146개의 소수가 등장
# print(len(primes))

result = 0

start = 0
end = 1
while end <= len(primes):
    s = sum(primes[start:end])
    if s == n:
        result += 1
        start += 1
    elif s < n:
        end += 1
    else:
        start += 1


print(result)
