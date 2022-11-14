import sys

input = sys.stdin.readline

N = int(input())

cars_entrance = {}
for i in range(N):
    cars_entrance[input()] = i

cars_exit = []
for _ in range(N):
    cars_exit.append((input()))

result = 0
for j in range(N - 1):
    for k in range(j + 1, N):
        if cars_entrance[cars_exit[j]] > cars_entrance[cars_exit[k]]:
            result += 1
            break
print(result)
