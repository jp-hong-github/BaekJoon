n, m = map(int, input().split())
times = list(map(int, input().split()))

start = 1
end = m * max(times)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        total += mid // times[i]

    if total >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
