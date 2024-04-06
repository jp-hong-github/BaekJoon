# cSpell:ignore Unknwon
import sys
import math

input = sys.stdin.readline

min_value, max_value = map(int, input().split())
if min_value > max_value:
    max_value, min_value = min_value, max_value

divisor, remainder = map(int, input().split())
if not (0 <= remainder < abs(divisor)):
    print("Unknwon Number")
    sys.exit()

divisor = abs(divisor)

min_value = math.ceil((min_value - remainder) / divisor)
max_value = math.floor((max_value - remainder) / divisor)

if max_value - min_value == 0:
    print(max_value * divisor + remainder)
else:
    print("Unknwon Number")
