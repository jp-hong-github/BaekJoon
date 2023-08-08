import sys

input = sys.stdin.readline
N, T, C, P = map(int, input().split())

print((N - 1) // T * C * P)
