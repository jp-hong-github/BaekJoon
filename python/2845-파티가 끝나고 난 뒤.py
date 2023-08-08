import sys

input = sys.stdin.readline

L, P = map(int, input().split())
num = list(map(int, input().split()))

people = L * P
for value in num:
    print(value - people, end=" ")
