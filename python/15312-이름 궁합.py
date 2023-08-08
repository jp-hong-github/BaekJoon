import sys

input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

alphabet_number = [
    3,
    2,
    1,
    2,
    3,
    3,
    2,
    3,
    3,
    2,
    2,
    1,
    2,
    2,
    1,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    1,
    2,
    2,
    1,
]

A_number = [alphabet_number[ord(i) - 65] for i in A]
B_number = [alphabet_number[ord(i) - 65] for i in B]
dp = []
temp = []
for i in range(len(A_number)):
    temp.append(A_number[i])
    temp.append(B_number[i])
dp.append(temp)

for i in range(len(A_number) + len(B_number) - 2):
    temp = []
    for dp_idx in range(len(dp[i]) - 1):
        temp.append((dp[i][dp_idx] + dp[i][dp_idx + 1]) % 10)
    dp.append(temp)

print(str(dp[-1][0]) + str(dp[-1][1]))
