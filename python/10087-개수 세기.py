import sys

input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
v = int(input())

result = 0
for num in num_list:
    if v == num:
        result += 1

print(result)
