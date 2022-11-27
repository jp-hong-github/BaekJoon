import sys
from itertools import product

input = sys.stdin.readline

N = int(input())
M = int(input())

if M > 0:
    not_work_btn = list(map(int, input().split()))
else:
    not_work_btn = []
work_btn = [x for x in range(10) if x not in not_work_btn]  # 작동 가능한 버튼들

result = abs(100 - N)

all_cases = []
for i in range(1, 7):
    all_cases.extend(list(product(work_btn, repeat=i)))

for case in all_cases:
    num = 0
    for k in range(len(case)):
        num += case[k]
        if k != (len(case) - 1):
            num *= 10
    result = min(result, abs(N - num) + len(case))

print(result)
