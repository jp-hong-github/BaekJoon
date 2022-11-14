import decimal
import sys

input = sys.stdin.readline

n = int(input())
stars = []
for _ in range(n):
    x, y = map(str, input().split())
    x = decimal.Decimal(x)
    y = decimal.Decimal(y)


def cal_dist(x1, y1, x2, y2):
    return decimal.Decimal.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
