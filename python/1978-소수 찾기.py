import sys

input = sys.stdin.readline

# cSpell:ignore sosu
prime_boolean = [False, False] + [True for _ in range(9999)]


for i in range(2, 1234):
    if prime_boolean[i]:
        for k in range(2 * i, 1234, i):
            prime_boolean[k] = False


n = int(input())
numbers = list(map(int, input().split()))

result = 0
for z in numbers:
    if prime_boolean[z]:
        result += 1

print(result)
