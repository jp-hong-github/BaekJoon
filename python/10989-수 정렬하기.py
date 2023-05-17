import sys

# bisect insort : 시간초과

input = sys.stdin.readline

n = int(input())

number_count = [0 for _ in range(10001)]

for _ in range(n):
    num = int(input())
    number_count[num] += 1

for idx, count in enumerate(number_count):
    if count == 0:
        continue

    for _ in range(count):
        print(idx)
