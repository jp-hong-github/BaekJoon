import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
result = 100_001
sum_of_num = 0

while True:
    if sum_of_num >= s:
        result = min(result, right - left)
        sum_of_num -= numbers[left]
        left += 1
    elif right == n:
        break
    else:
        sum_of_num += numbers[right]
        right += 1


if result == 100_001:
    print(0)
else:
    print(result)
