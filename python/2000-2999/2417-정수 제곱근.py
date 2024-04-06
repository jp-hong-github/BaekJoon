import sys

input = sys.stdin.readline
n = int(input())

start = 0
end = n
result = 0

while start <= end:
    mid = (start + end) // 2
    # print(start, end, mid, mid ** 2, n)

    temp = mid**2
    if temp == n:
        result = mid
        break
    elif temp > n:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
