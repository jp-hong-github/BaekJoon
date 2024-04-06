import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


perfect_square_numbers = []
for i in range(1, 10001):
    perfect_square_numbers.append(i**2)

result = []
for i in perfect_square_numbers:
    if n <= i <= m:
        result.append(i)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
