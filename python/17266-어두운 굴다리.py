import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
x_list = list(map(int, input().split()))

result = 0

mid = 0
for i in range(M - 1):
    if (x_list[i + 1] - x_list[i]) % 2 == 0:
        temp = (x_list[i + 1] - x_list[i]) // 2
    else:
        temp = (x_list[i + 1] - x_list[i]) // 2 + 1
    if mid < temp:
        mid = temp

result = max(x_list[0], mid, N - x_list[-1])  # 맨 처음 사이, 중간 사이 중 가장 큰 값, 맨 마지막 사이
print(result)
