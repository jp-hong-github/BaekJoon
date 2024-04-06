import sys

input = sys.stdin.readline


N = int(input())

dp = []
dp.append([0, 0, 0])
# 1. 아무데도 넣지 않을 때
# 2. 왼쪽 타일에만 사자를 넣을 떄
# 3. 오른쪽 타일에만 사자를 넣을 때
dp.append([1, 1, 1])

for i in range(2, N + 1):
    dp.append(
        [
            (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901,  # 아무데도 넣지 않을 때
            (dp[i - 1][0] + dp[i - 1][1]) % 9901,  # 오른쪽에 넣었을 때
            (dp[i - 1][0] + dp[i - 1][2]) % 9901,  # 왼쪽에 넣었을 떄
        ]
    )

print(sum(dp[N]) % 9901)
