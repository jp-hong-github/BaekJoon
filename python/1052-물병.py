import sys

input = sys.stdin.readline

N, K = map(int, input().split())

result = 0
while bin(N).count("1") > K:
    idx = bin(N)[::-1].index("1")
    result += 2**idx
    N += 2**idx
print(result)
