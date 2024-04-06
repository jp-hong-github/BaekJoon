import sys

input = sys.stdin.readline

n = int(input())
sum = 1
temp = 1
while True:
    if n <= sum:
        print(temp)
        break
    sum += temp * 6
    temp += 1
