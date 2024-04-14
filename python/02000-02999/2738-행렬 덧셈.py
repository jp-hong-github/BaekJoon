import sys

input = sys.stdin.readline
N, M = map(int, input().split())

result = []

for _ in range(N):
    result.append(list(map(int, input().split())))

for i in range(N):
    temp = list(map(int, input().split()))
    for k in range(M):
        result[i][k] += temp[k]

for e in result:
    print(*e)
