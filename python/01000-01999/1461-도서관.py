import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))
books = list(map(int, input().split()))

if n == 1:  # 책이 한 권
    print(books[0])

elif n == 2:  # 책이 두 권
    book_1 = books[0]
    book_2 = books[1]
    if (book_1 > 0 and book_2 < 0) or (book_1 < 0 and book_2 > 0):  # 원점에서 각기 다른 방향
        print(min(abs(book_1), abs(book_2)) * 2 + max(abs(book_1), abs(book_2)))
    else:  # 원점에서 같은 방향
        print(max(abs(book_1), abs(book_2)))

else:  # 책이 세 권이상
    max_dist = 0
    left_zero = []  # 0에서 왼쪽
    right_zero = []  # 0에서 오른쪽
    for book in books:
        max_dist = max(max_dist, abs(book))
        if book < 0:
            left_zero.append(book)
        else:
            right_zero.append(book)

    left_zero.sort()
    right_zero.sort(reverse=True)

    result = 0

    for i in range(0, len(left_zero), m):
        result += abs(left_zero[i]) * 2
    for i in range(0, len(right_zero), m):
        result += right_zero[i] * 2

    print(result - max_dist)

# ! 너무 복잡하여 폐기
# =============================================================================================== #


# # 마지막 책을 옮기는 경우를 미리 계산
# if abs(left_zero[0]) > abs(right_zero[-1]):  # 원점에서 왼쪽으로 더 멀리 떨어져 있는 경우
#     result = abs(left_zero[0])
#     for _ in range(min(m, len(left_zero))):
#         left_zero.popleft()
# elif abs(left_zero[0]) < abs(right_zero[-1]):  # 원점에서 오른쪽으로 더 멀리 떨어져 있는 경우
#     result = abs(right_zero[-1])
#     for _ in range(min(m, len(right_zero))):
#         right_zero.pop()
# elif abs(left_zero[0]) == abs(right_zero[-1]):  # 원점에서 같은 거리만큼 떨어져 있는 경우
#     if len(left_zero) > len(right_zero):  # 왼쪽에 더 많은 책이 있는 경우
#         result = abs(left_zero[0])
#         for _ in range(min(m, len(left_zero))):
#             left_zero.popleft()
#     elif len(left_zero) < len(right_zero):  # 오른쪽에 더 많은 책이 있는 경우
#         result = abs(right_zero[-1])
#         for _ in range(min(m, len(right_zero))):
#             right_zero.pop()
#     else: # 양쪽의 책의 개수가 같을 경우


# # 옮기지 않은 책을 옮김
# while left_zero:
#     result += abs(left_zero[0]) * 2
#     for _ in range(min(m, len(left_zero))):
#         left_zero.popleft()

# while right_zero:
#     result += right_zero[-1] * 2
#     for _ in range(min(m, len(right_zero))):
#         right_zero.pop()

# print(result)
# =============================================================================================== #
