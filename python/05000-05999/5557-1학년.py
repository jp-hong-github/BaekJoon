import sys

input = sys.stdin.readline

n = int(input())
numbers: list = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n - 1)]

dp[0][numbers[0]] = 1

for idx in range(1, n - 1):
    for value in range(21):
        if dp[idx - 1][value] != 0:
            # 뺼셈 연산
            if value - numbers[idx] >= 0:
                dp[idx][value - numbers[idx]] += dp[idx - 1][value]

            # 덧셈 연산
            if value + numbers[idx] <= 20:
                dp[idx][value + numbers[idx]] += dp[idx - 1][value]

print(dp[-1][numbers[-1]])
