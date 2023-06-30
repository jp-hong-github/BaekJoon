import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trains = [0 for _ in range(n + 1)]
orders = [list(map(int, input().split())) for _ in range(m)]

for order in orders:
    if order[0] == 1:
        mask = 1 << order[2]
        trains[order[1]] |= mask
    elif order[0] == 2:
        mask = ~(1 << order[2])
        trains[order[1]][order[2]] &= mask
    elif order[0] == 3:
        trains[order[1]] = trains[order[1]] << 1
    elif order[0] == 4:
        trains[order[1]] = trains[order[1]] >> 1

result = len(list(set(trains[1:])))
print(result)

# ! 코드 작성할 때부터 시간 초과가 날 거라고 예상함
# False는 빈자리, True는 사람이 앉음
# seats = [deque([False for _ in range(21)]) for _ in range(n + 1)]

# orders = [list(map(int, input().split())) for _ in range(m)]

# # 명령 수행
# for order in orders:
#     if order[0] == 1:
#         seats[order[1]][order[2]] = True
#     elif order[0] == 2:
#         seats[order[1]][order[2]] = False
#     elif order[0] == 3:
#         seats[order[1]].appendleft(False)
#         seats[order[1]].pop()

#     elif order[0] == 4:
#         seats[order[1]].append(False)
#         seats[order[1]].popleft()

# # 기차 확인
# result = 0
# for i in range(1, n - 1):
#     isOk = 0
#     for s in range(i + 1, n):
#         for j in range(20):
#             if seats[s][j] == seats[i][j]:
#                 isOk += 1

#     if isOk != 20:
#         result += 1

# print(result)
