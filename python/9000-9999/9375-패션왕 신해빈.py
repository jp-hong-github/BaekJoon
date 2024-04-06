import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

t = int(input())

answer_list = []
for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)
    for _ in range(n):
        name, kind = list(map(str, input().split()))
        clothes[kind] += 1

    answer = 1
    # key = clothes.keys()
    # for i in range(1, len(key) + 1):
    #     cases = list(combinations(key, i))
    #     # print(cases)
    #     for case in cases:  # ex : case = (1,2,3,4)
    #         temp = 1
    #         for k in case:
    #             temp *= clothes[k]

    #         answer += temp
    for key in clothes.keys():
        answer *= clothes[key] + 1
    answer_list.append(answer - 1)

for answer in answer_list:
    print(answer)
