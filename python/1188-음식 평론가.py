import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())
print(M - math.gcd(N, M))
