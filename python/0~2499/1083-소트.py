import sys

input = sys.stdin.readline

# 1<= N <= 50
N = int(input())
numbers = list(map(int, input().split()))
# 0<= S <= 1_000_000
s = int(input())


current_idx = 0
while current_idx < N:
    if s == 0:
        break
    current_max_num = numbers[current_idx]
    max_idx = current_idx
    for i in range(current_idx, min(current_idx + s + 1, N)):
        if current_max_num < numbers[i]:
            current_max_num = numbers[i]
            max_idx = i
    # print(numbers[current_idx], numbers[max_idx])
    # print(s, current_idx, numbers, "\n")
    if max_idx == current_idx:
        pass
    else:
        s -= max_idx - current_idx
        numbers.remove(current_max_num)
        numbers.insert(current_idx, current_max_num)

    current_idx += 1


print(*numbers)
