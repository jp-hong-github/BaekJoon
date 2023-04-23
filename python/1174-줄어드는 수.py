import sys

input = sys.stdin.readline

N = int(input())
numbers = [[0]]


def dfs(current_digit, max_digit, value, numList):
    if current_digit == max_digit:
        numbers.append(numList.copy())
    else:
        for next_value in range(0, value):
            numList.append(next_value)
            dfs(current_digit + 1, max_digit, next_value, numList)
            numList.pop()


for max_digit in range(1, 11):
    for value in range(1, 10):
        dfs(1, max_digit, value, [value])

if len(numbers) < N:
    print(-1)
else:
    for i in numbers[N - 1]:
        print(i, end="")
