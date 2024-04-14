import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a_set = set(list(map(int, input().split())))
b_set = set(list(map(int, input().split())))

print(len(a_set - b_set) + len(b_set - a_set))
