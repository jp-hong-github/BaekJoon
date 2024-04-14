n, m = map(int, input().split())

lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)

while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 0
    for i in range(n):
        if total + lesson[i] > mid:
            total = 0
            count += 1
        total += lesson[i]

    if total != 0:  # 마지막 카운트
        count += 1

    if count <= m:
        end = mid - 1

    else:
        start = mid + 1
print(start)
