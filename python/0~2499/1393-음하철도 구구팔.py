import sys
import math

input = sys.stdin.readline


x_s, y_s = map(int, input().split())

x_e, y_e, dx, dy = map(int, input().split())
gcd = math.gcd(dx, dy)

t = 0
min_dst = int(10e9)
pre_min_dst = min_dst
x_result = 0
y_result = 0
while True:
    x_n = x_e + int((t / gcd) * dx)
    y_n = y_e + int((t / gcd) * dy)
    cal_dist = (x_s - x_n) ** 2 + (y_s - y_n) ** 2
    min_dst = min(min_dst, cal_dist)
    if min_dst == pre_min_dst:
        print("%d %d" % (x_result, y_result))
        break
    else:
        pre_min_dst = min_dst
        x_result = x_n
        y_result = y_n
    t += 1
