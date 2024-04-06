import sys
from collections import Counter
import decimal

# cSpell:ignore getcontext
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

print(round(sum(numbers) / N))
print(sorted(numbers)[N // 2])

count_dict = Counter(numbers)

most_frequent = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

if len(most_frequent) > 1 and most_frequent[0][1] == most_frequent[1][1]:
    result = sorted([mf[0] for mf in most_frequent if mf[1] == most_frequent[0][1]])[1]
else:
    result = most_frequent[0][0]
print(result)
print(max(numbers) - min(numbers))
