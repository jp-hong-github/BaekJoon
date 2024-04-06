import bisect
import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

# 시간 복잡도 : O(n**2)
# array = [1] * n

# for i in range(n - 1):
#     for k in range(i + 1, n):
#         if data[k] > data[i]:
#             if array[k] < array[i] + 1:
#                 array[k] = array[i] + 1

# print(max(array))


# 시간 복잡도 : O(n log n)
def lis(arr):
    n = len(arr)
    ends = [arr[0]]

    for num in arr[1:]:
        if num > ends[-1]:
            ends.append(num)
        else:
            idx = bisect.bisect_left(ends, num)
            ends[idx] = num

    return ends


print(len(lis(data)))
