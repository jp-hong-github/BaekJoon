import sys

input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))  # d
pizza_list = list(map(int, input().split()))  # n

previous_max_value = oven[0]
# oven = [5,6,4,3,6,2,3]을 [5,5,4,3,3,2,2]으로 바꾸고 이분 탐색 진행
for i in range(d):
    if oven[i] > previous_max_value:
        oven[i] = previous_max_value
    else:
        previous_max_value = oven[i]


def binary_search(start, end, search_value):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if oven[mid] >= search_value:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result


answer = -1
end_idx = d - 1
for i, pizza in enumerate(pizza_list):
    idx = binary_search(0, end_idx, pizza)
    if (i != n - 1 and idx == 0) or idx == -1:
        answer = 0
        break
    end_idx = idx - 1
    answer = idx + 1

print(answer)
