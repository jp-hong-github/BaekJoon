import sys

from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP

getcontext().prec = 999
input = sys.stdin.readline

t = int(input())
digit_num = "." + "".join([str(0) for _ in range(900)]) + "1"
result_list = []
for _ in range(t):
    num = Decimal(input())

    approximate_cube_root = num ** (Decimal("1") / Decimal("3"))

    approximate_cube_root = Decimal(approximate_cube_root).quantize(Decimal(digit_num), rounding=ROUND_HALF_UP)
    result_list.append(approximate_cube_root)

for r in result_list:
    r = Decimal(r).quantize(Decimal(".0000000001"), rounding=ROUND_DOWN)
    print(r)
