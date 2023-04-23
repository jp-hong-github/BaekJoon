import sys

input = sys.stdin.readline

n, k = map(int, input().split())
drink = [int(input()) for _ in range(n)]


start = 0
end = max(drink)
result = 0
while start <= end:
    mid = (start + end) // 2  # 술의 양
    num_of_cups = 0
    if mid == 0:
        if start == 0 and end == 1:
            mid = 1
        else:
            break
    #print(start, mid, end, end=" ")
    for i in drink:
        num_of_cups += i // mid
    #print(num_of_cups)
    if num_of_cups >= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
