import sys

input = sys.stdin.readline

n = int(input())

numbers: list = list(map(int, input().split()))
numbers_sort = {v: i for i, v in enumerate(sorted(list(set(numbers))))}

result = []
for num in numbers:
    result.append(numbers_sort[num])

print(*result)
