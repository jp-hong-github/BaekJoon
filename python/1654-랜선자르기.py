k, n = map(int, input().split())

import sys

lan_sun = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lan_sun)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for k in lan_sun:
        total += k // mid
        # if k%mid == mid:
        #    total+=mid
    if total >= n:
        start = mid + 1
        if mid > result:
            result = mid
    else:
        end = mid - 1

print(result)
