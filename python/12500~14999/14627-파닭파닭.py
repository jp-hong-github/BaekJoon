import sys

input = sys.stdin.readline

S, C = map(int, input().split())
pa_list = [int(input()) for i in range(S)]

start = 1
# end = min(pa_list)
end = max(pa_list)

max_pa_len = 0

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    remainder = 0
    pa_count = 0
    for pa in pa_list:
        pa_count += pa // mid
        remainder += pa % mid

    if pa_count < C:
        end = mid - 1
    elif pa_count >= C:
        if max_pa_len < mid:
            max_pa_len = mid
        start = mid + 1


print(sum(pa_list) - C * max_pa_len)
