"""
1. 치킨 집 위치 파악
2. m개의 치킨 집 선택
3. 치킨 거리 계산
"""

# n,m = map(int,input().split())
# house = []
# chicken = []

# for i in range(n):
#     temp = list(map(int,input().split()))
#     for k in range(n):
#         if temp[k]==2:#치킨집인 경우
#             chicken.append([i,k])
#         if temp[k]==1:#가정집인 경우
#             house.append([i,k])

# chiken_distance = [0]*(len(house))#모든 치킨집의 치킨 거리를 구함

# for idx in range(len(house)):
#     temp=[]
#     for c in chicken:
#         temp.append(abs(house[idx][0]-c[0]) + abs(house[idx][1]-c[1]))

# print(chiken_distance)
# chiken_distance.sort()
# print(sum(chiken_distance[:m]))

from itertools import combinations

n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    temp = list(map(int, input().split()))
    for k in range(n):
        if temp[k] == 2:  # 치킨집인 경우
            chicken.append([i, k])
        if temp[k] == 1:  # 가정집인 경우
            house.append([i, k])

cases = list(combinations(chicken, m))  # m개를 뽑는 경우의 수

result = [0] * len(cases)
i = 0
for case in cases:
    for idx in range(len(house)):
        case_result = 999999999999999999999999
        temp = []
        for c in case:
            temp.append(abs(house[idx][0] - c[0]) + abs(house[idx][1] - c[1]))
        case_result = min(case_result, min(temp))
        result[i] += case_result
    i += 1
print(min(result))
