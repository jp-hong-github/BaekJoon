import sys

input = sys.stdin.readline

N = int(input())


result = 1
for i in range(1, N + 1):
    result *= i
    while result % 10 == 0:
        result //= 10
    if result >= 1000000000000:
        result %= 1000000000000

result %= 100000
print("%05d" % result)
