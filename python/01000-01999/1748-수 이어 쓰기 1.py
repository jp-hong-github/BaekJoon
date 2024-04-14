import sys

input = sys.stdin.readline

N = int(input())
number = 100_000_000
result = 0


while number != 0:
    if len(str(N)) >= len(str(number)):
        result += len(str(number)) * (N - number + 1)
        N = number - 1
    number //= 10


print(result)
