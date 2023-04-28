import sys

input = sys.stdin.readline

A, B = list(map(int, input().split()))

# 1. 우선 범위 내의 4와 7로만 이루어진 수를 전부 만든다.
# 2. 이분 탐색을 통해 A이상인 수와 B이하인 금민수를 구한다.
# 3. 그 사이의 숫자의 개수를 구한다.

# 4,7,44,47,74,77,444...

num_list = ["4", "7"]

idx = 0
number = num_list[idx]

while True:
    if int(number + "4") > 1000000000:
        break
    num_list.append(number + "4")
    num_list.append(number + "7")
    idx += 1
    number = num_list[idx]

# 단순히 전부 찾아보는 경우 num_list의 원소의 개수가 약 1000개이므로 가능
count = sum(A <= int(x) <= B for x in num_list)
# print(count)


# 이분 탐색 사용
def binary_search_count(num_list, A, B):
    left = 0
    right = len(num_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if int(num_list[mid]) < A:
            left = mid + 1
        else:
            right = mid - 1
    start_index = left

    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if int(num_list[mid]) > B:
            right = mid - 1
        else:
            left = mid + 1
    end_index = right
    # print(start_index, end_index)
    return end_index - start_index + 1


print(binary_search_count(num_list, A, B))
