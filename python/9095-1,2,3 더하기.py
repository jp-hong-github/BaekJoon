import sys

input = sys.stdin.readline

T = int(input())


dp = [0]  # 각 인덱스를 만드는 방법의 개수의 리스트
dp.append(1)
dp.append(2)
dp.append(4)

for a in range(4, 11):
    dp.append(dp[a - 3] + dp[a - 2] + dp[a - 1])  # 각각 맨 앞의 숫자가 3,2,1일 때로 하여 만드는 방법

# print(dp)

for _ in range(T):
    num = int(input())
    print(dp[num])

