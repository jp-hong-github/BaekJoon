import sys
import heapq

input = sys.stdin.readline

N = int(input())
house = list(map(int, input().split()))
result = 0


# 최소 힙을 사용
house_sorted = []
for s in house:
    heapq.heappush(house_sorted, -s)

total_house = N  # 현재 눈이 남아 있는 집의 개수
while house_sorted:
    if total_house > 1:  # 현재 눈을 전부 치우지 않은 집의 개수가 2개 이상인 경우
        temp_house1 = heapq.heappop(house_sorted)
        temp_house2 = heapq.heappop(house_sorted)

        for temp_house in [temp_house1, temp_house2]:
            if temp_house == -1:
                total_house -= 1
            else:
                heapq.heappush(house_sorted, temp_house + 1)

    elif total_house == 1:  # 현재 눈을 전부 치우지 않은 집의 개수가 1개인 경우
        temp_house = heapq.heappop(house_sorted)
        if temp_house == -1:
            total_house -= 1
        else:
            heapq.heappush(house_sorted, temp_house + 1)

    result += 1
    # print(result, house_sorted)

if result > 1440:
    print(-1)
else:
    print(result)
