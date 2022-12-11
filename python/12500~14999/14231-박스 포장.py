import sys


input = sys.stdin.readline
n = int(input())
boxes = list(map(int, input().split()))
dp = [1 for _ in range(n)]
# for i, box in enumerate(boxes):
#     if i == 0:
#         dp.append(1)
#     else:
#         if boxes[i - 1] < box:
#             dp.append(dp[i - 1] + 1)
#         else:
#             dp.append(1)

# print(max(dp))
# print(dp)

# 바로 앞이 아니라 앞에 있는 어떤 박스든 가능
for i, box in enumerate(boxes):
    if i == 0:
        continue
    else:
        for k in range(i):
            if box > boxes[k]:
                dp[i] = max(dp[i], dp[k] + 1)

print(max(dp))
# print(dp)
