import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))


def binary_search(arr, val):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return mid
    return low


def longest_increasing_subsequence(seq):
    tails = []

    for num in seq:
        index = binary_search(tails, num)

        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num

    return len(tails)


length = longest_increasing_subsequence(numbers)
print(length)
