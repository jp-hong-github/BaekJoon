import sys

input = sys.stdin.readline

N = int(input())
data = [1, 5, 10, 50]


########################################################################
"""중복 조합 라이브러리를 이용하는 방법"""

# from itertools import combinations_with_replacement

# temp_comb = combinations_with_replacement(data, N)

# check = set()
# for i in temp_comb:
#     check.add(sum(i))
# print(len(check))
########################################################################
sumList = [0] * 1001  # N이 20이하 이므로 50*20 = 1000 즉 최댓값은 1000임


def rome_char(count, arr, value):
    # print("count : ", count, "arr : ", arr)
    if count == N:
        sumList[sum(arr)] = 1
    else:
        for i in data:
            if i >= value:
                arr.append(i)
                rome_char(count + 1, arr, i)
                arr.pop()


result = set()
for i in data:
    arr = [i]
    rome_char(1, arr, i)
print(sum(sumList))
