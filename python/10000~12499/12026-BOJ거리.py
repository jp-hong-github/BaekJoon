import sys

input = sys.stdin.readline


n = int(input())
street = input()

dp = [float("inf")] * (n + 1)

# B이면 O를 만났을 때 종료, O이면 J를 만날 때까지, J이면 B를 만날 때까지
def get_prev(x):
    if x == "B":
        return "J"
    elif x == "J":
        return "O"
    elif x == "O":
        return "B"


dp[0] = 0
for i in range(1, n):
    prev = get_prev(street[i])
    for j in range(i):
        if street[j] == prev:  # b다음에 o 식으로 들어왔을 때
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

print(dp[n - 1] if dp[n - 1] != float("inf") else -1)

