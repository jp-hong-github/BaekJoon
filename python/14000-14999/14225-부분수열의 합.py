import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

number_sum_set = set()

for i in range(1, n + 1):
    comb = combinations(numbers, i)
    for case in comb:
        number_sum_set.add(sum(case))

number_sum_list = sorted(list(number_sum_set))


check = True  # 모든 자연수가 인덱스만큼 있는 경우
# 예 : [1,2,3]의 경우 정답은 4
for i in range(0, len(number_sum_list)):
    if i + 1 != number_sum_list[i]:
        print(i + 1)
        check = False
        break

if check:
    print(len(number_sum_list) + 1)

# print(number_sum_list)
# ================================================================= #
# & 총 경우의 수 : 1048575

# import math

# all_case = 0
# for i in range(1, 21):
#     all_case += math.comb(20, i)

# print(all_case)
