import sys

input = sys.stdin.readline

n, k = map(int, input().split())

children = list(map(int, input().split()))

# 1 3 5 6 10의 경우
# 1 3, 5 6, 10으로 나누면 3의 비용이 듬

# 1 4 5 6 10의 경우
# 1, 4 5 6, 10으로 나누면 2의 비용이 듬

dif = []
for i in range(1, n):
    dif.append(children[i] - children[i - 1])

dif.sort()
result = 0
for i in range(n - k):
    result += dif[i]

print(result)
