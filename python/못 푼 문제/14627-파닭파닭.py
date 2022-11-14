import sys

input = sys.stdin.readline
S, C = map(int, input().split())

vegetable = []
for _ in range(S):
    temp = int(input())
    vegetable.append(temp)

start = 0
end = min(vegetable)

final_remainder = 0
while start <= end:
    mid = (start + end) // 2
    remainder = 0
    count = 0
    # print(start, mid, end)
    for var in vegetable:
        if count != C:
            while var >= mid:
                var -= mid
                count += 1
                if count == C:
                    break
            remainder += var
        else:
            remainder += var

    if count > C:
        start = mid + 1
    elif count == C:
        start = mid + 1
        final_remainder = remainder
    else:
        end = mid - 1

print(final_remainder)
