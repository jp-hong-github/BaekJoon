import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num_sort = sorted(num)

result = []
for idx, val in enumerate(num):
    idx_val = num_sort.index(val)
    result.append(idx_val)
    num_sort[idx_val] = -1
print(*result)
# print(num_sort)
