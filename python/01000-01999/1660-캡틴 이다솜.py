import sys

input = sys.stdin.readline

n = int(input())

triangle = [0]  # 삼각형의 필요한 대포알의 개수
tetrahedron = [0]  # 사면체의 필요한 대포알의 개수

i = 1
while tetrahedron[-1] < n:
    triangle.append(triangle[i - 1] + i)
    tetrahedron.append(tetrahedron[i - 1] + triangle[i])
    i += 1

result = 0

dp = [int(10e9) for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1
for q in range(1, n + 1):
    for k in range(0, i):
        if q - tetrahedron[k] >= 0:
            dp[q] = min(dp[q], dp[q - tetrahedron[k]] + 1)

print(dp[n])
