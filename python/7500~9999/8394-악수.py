import sys

input = sys.stdin.readline
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(3)
else:
    dp_a = 2
    dp_b = 3
    result = 0
    for i in range(4, n + 1):
        result = (dp_a % 10 + dp_b % 10) % 10
        dp_a = dp_b % 10
        dp_b = result

    print(result)
