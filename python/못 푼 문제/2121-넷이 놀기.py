import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

coordinate = []
for _ in range(n):
    coordinate.append(list(map(int, input().split())))

