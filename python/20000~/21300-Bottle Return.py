import sys

input = sys.stdin.readline

bottle = list(map(int, input().split()))
print(sum(bottle)*5)
