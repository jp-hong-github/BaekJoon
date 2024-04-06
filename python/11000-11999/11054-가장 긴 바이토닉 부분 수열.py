import sys
import bisect

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))


def get_lis_len(arr, max_num):
    # 빈 배열인 경우
    if not arr:
        return 0

    lis = []

    for num in arr:
        if num >= max_num:
            continue

        elif not lis:
            lis.append(num)

        elif num > lis[-1]:
            lis.append(num)
        else:
            idx = bisect.bisect_left(lis, num)
            lis[idx] = num

    return len(lis)


result = 0
for idx, number in enumerate(numbers):
    # 여기서 number변수를 중앙에 위치하는 가장 큰 값으로 지정함
    left_lis_len = get_lis_len(numbers[:idx], number)
    right_lis_len = get_lis_len(list(reversed(numbers[idx + 1 :])), number)
    # print(idx, number, left_lis_len, right_lis_len)
    result = max(result, left_lis_len + right_lis_len + 1)

print(result)
