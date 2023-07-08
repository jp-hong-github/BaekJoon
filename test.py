import sys

input = sys.stdin.readline
# 246912 = 123456*2
prime_check = [False, False] + [True for _ in range(250000)]

for i in range(2, int(250000 ** (0.5)) + 1):
    if prime_check[i]:
        for k in range(i + i, 250000, i):
            prime_check[k] = False


while 1:
    n = int(input())
    if n == 0:
        break

    answer = 0
    for i in range(n + 1, 2 * n + 1):
        if prime_check[i] == True:
            answer += 1

    print(answer)
