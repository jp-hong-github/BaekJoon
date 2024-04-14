import sys

input = sys.stdin.readline

result = 0
A, B = map(int, input().split())

# 에라토스테네스의 채
n = 100000
a = [True] * (n + 1)
primes = []  # 소수 집합

for i in range(2, n + 1):
    if a[i] == True:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

primes_list_length = len(primes)

for num in range(A, B + 1):
    num_temp = num
    idx = 0
    count_prime = 0
    while idx < primes_list_length and primes[idx] <= num:
        if num % primes[idx] == 0:
            num /= primes[idx]
            count_prime += 1
        else:
            idx += 1
    if num == 1 and count_prime in primes:
        result += 1
        # print(num_temp)

print(result)
