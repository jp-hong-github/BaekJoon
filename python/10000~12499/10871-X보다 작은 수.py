import sys

input = sys.stdin.readline
n, x = map(int, input().split())

num_list = list(map(int, input().split()))

result = []
for i in num_list:
    if i<x:
        result.append(i)
        
print(*result)