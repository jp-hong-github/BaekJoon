import sys
from collections import Counter

input = sys.stdin.readline

point_1 = list(map(int, input().split()))
point_2 = list(map(int, input().split()))
point_3 = list(map(int, input().split()))

x, y = point_1[0], point_1[1]

if x == point_2[0]:
    x = point_3[0]
elif x == point_3[0]:
    x = point_2[0]

if y == point_2[1]:
    y = point_3[1]
elif y == point_3[1]:
    y = point_2[1]

print(x, y)

