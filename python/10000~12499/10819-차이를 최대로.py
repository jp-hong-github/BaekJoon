import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

answer = 0

comb = list(permutations(numbers, N))

for case in comb:
    # print(case, end=" ")
    sum = 0
    for idx, num in enumerate(case):
        if idx == N - 1:
            answer = max(answer, sum)
            # print(sum)
        else:
            sum += abs(case[idx] - case[idx + 1])

print(answer)
