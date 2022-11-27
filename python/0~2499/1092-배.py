import sys
import bisect

input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

if max(crane) < max(box):
    print(-1)
else:
    crane.sort(reverse=True)
    box.sort()

    result = 0
    moved_box_count = 0

    while box:
        for c in crane:
            right = bisect.bisect_right(box, c)
            if box and box[right-1] <= c:
                box.pop(right-1)

        result += 1
    print(result)
