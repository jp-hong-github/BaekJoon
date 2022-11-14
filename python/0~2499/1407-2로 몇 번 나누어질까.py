import sys

input = sys.stdin.readline


def calculate(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value % 2 == 0:
        return value // 2 + 2 * calculate(value // 2)
    else:
        return value // 2 + 2 * calculate(value // 2) + 1


A, B = map(int, input().split())
result = calculate(B) - calculate(A - 1)
print(result)
