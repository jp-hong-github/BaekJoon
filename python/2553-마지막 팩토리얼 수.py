import sys

input = sys.stdin.readline

n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i

result = str(result)
for num in result[::-1]:
    if int(num) != 0:
        print(num)
        break
