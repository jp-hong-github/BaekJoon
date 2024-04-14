import sys
from itertools import combinations

input = sys.stdin.readline


N = int(input())
taste = []
for i in range(N):
    taste.append(list(map(int, input().split())))

idx_list = [i for i in range(0, N)]
result = int(10e10)
for k in range(1, N + 1):
    comb = list(combinations(idx_list, k))
    for case in comb:
        s_temp = 1
        b_temp = 0
        for j in case:
            s_temp *= taste[j][0]
            b_temp += taste[j][1]
        result_temp = abs(s_temp - b_temp)
        result = min(result, result_temp)

print(result)
