import sys

input = sys.stdin.readline

n = input()
n = int(n, 2)
n *= 17
print(bin(n)[2:])
