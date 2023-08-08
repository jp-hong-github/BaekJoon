n, k = map(int, input().split())
levels = []
for i in range(n):
    levels.append(int(input()))

result = 0
start = 1
end = 1000000001

while start <= end:
    count = k
    mid = (start + end) // 2
    for lv in levels:
        if lv < mid:
            count -= mid - lv
            if count < 0:
                break
    if count < 0:
        end = mid - 1
    elif count >= 0:
        result = mid
        start = mid + 1

print(result)
