import sys

input = sys.stdin.readline

N = int(input())
recommend_len = int(input())
recommend_lst = list(map(int, input().split()))

# 첫번째 값 : 추천받은 회수
# 두번째 값 : 언재 추천받았는지의 for문의 인덱스
# 세번째 값 : 누구

photo = []

for idx, rec in enumerate(recommend_lst):
    if len(photo) == 0:
        photo.append([1, idx, rec])

    elif len(photo) < N:
        if rec not in list(zip(*photo))[-1]:
            photo.append([1, idx, rec])
        else:
            for i in range(len(photo)):
                if photo[i][2] == rec:
                    photo[i][0] += 1
                    break

    else:
        if rec not in list(zip(*photo))[-1]:
            photo.sort()
            del photo[0]
            photo.append([1, idx, rec])
        else:
            for i in range(len(photo)):
                if photo[i][2] == rec:
                    photo[i][0] += 1
                    break


result = list(list(zip(*photo))[-1])
result.sort()
print(*result)

