import sys

input = sys.stdin.readline

n = int(input())

max_n = 1003001 + 1

# 소수 판별
sieve_of_eratosthenes = [False, False] + [True] * (max_n - 1)

for i in range(2, max_n + 1):
    if sieve_of_eratosthenes[i] == True:
        for j in range(2 * i, max_n + 1, i):
            sieve_of_eratosthenes[j] = False

# 팰린드롬 판별
for k in range(n, max_n, 1):
    if sieve_of_eratosthenes[k] == True:
        original_num = list(str(k))
        reverse_num = list(str(k))
        reverse_num.reverse()
        if original_num == reverse_num:
            print(k)
            break

