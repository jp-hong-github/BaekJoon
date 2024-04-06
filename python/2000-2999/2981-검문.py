import sys
import math

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

for i in range(n - 1):
    if i == 0:
        gcd = numbers[i + 1] - numbers[i]
    else:
        gcd = math.gcd(gcd, numbers[i + 1] - numbers[i])

result = []
for i in range(1, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.append(i)
        if i != gcd // i:
            result.append(gcd // i)

result = sorted(result)
result.remove(1)
print(*result)
