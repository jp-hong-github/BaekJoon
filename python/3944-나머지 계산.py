import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    B, D = map(str, input().split())
    result = 0
    B = int(B)
    for i in range(len(D)):
        result += int(D[i]) % (B - 1)
        result %= B - 1
    print(result)
