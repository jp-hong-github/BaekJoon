import sys
import math

input = sys.stdin.readline

x, y = list(map(int, input().split()))


print(x + y - math.gcd(x, y))
