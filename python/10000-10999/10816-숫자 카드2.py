# import sys

# input = sys.stdin.readline

# n = int(input())
# num = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))

# num.sort()
# result = []
# for value in check:
#     start = 0
#     end = n - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if num[mid] >= value:
#             if mid - 1 >= 0 and num[mid] == value and num[mid - 1] != value:
#                 break
#             end = mid - 1
#         else:
#             start = mid + 1
#     count = 0
#     while True:

#         if mid <= n - 1 and num[mid] == value:
#             count += 1
#             mid += 1
#         else:
#             break
#     result.append(count)

# print(*result)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# 출처: https://kongpowder.tistory.com/127 [차곡차곡]


n = int(input())
arr1 = list(map(int, input().split()))
dict1 = dict()  # 숫자카드와 개수를 딕셔너리에 담기
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
m = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in dict1:
        print(dict1[i], end=" ")  # 존재하는 숫자 카드라면
    else:
        print(0, end=" ")  # 존재하지 않는 숫자 카드라면
