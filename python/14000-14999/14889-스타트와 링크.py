import sys
from itertools import combinations

# import math

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# for i in range(2, 21, 2):
#     print(f"{i}명에서 {i//2}명을 선택하는 조합의 수 : ", math.comb(i, i // 2))

# 2명에서 1명을 선택하는 조합의 수 :  2
# 4명에서 2명을 선택하는 조합의 수 :  6
# 6명에서 3명을 선택하는 조합의 수 :  20
# 8명에서 4명을 선택하는 조합의 수 :  70
# 10명에서 5명을 선택하는 조합의 수 :  252
# 12명에서 6명을 선택하는 조합의 수 :  924
# 14명에서 7명을 선택하는 조합의 수 :  3432
# 16명에서 8명을 선택하는 조합의 수 :  12870
# 18명에서 9명을 선택하는 조합의 수 :  48620
# 20명에서 10명을 선택하는 조합의 수 :  184756


# 한 팀의 능력치의 게산
def cal_ability(team):
    team = tuple(team)
    ability_sum = 0
    for player in team:
        for other_player in team:
            if player != other_player:
                ability_sum += graph[player][other_player]

    return ability_sum


result = float("inf")

team_cases = list(combinations([i for i in range(N)], N // 2))
team_cases_len = len(team_cases)
for idx, team in enumerate(team_cases):
    # 4명 중에서 0번 선수와 1번 선수를 A팀으로 묶으면
    # B팀에는 2번 선수와 3번 선수가 속함
    # 그런데 2번 선수와 3번 선수를 A팀으로 묶으면
    # B팀에는 0번 선수와 1번 선수가 속함
    # 그러나 A팀과 B팀을 구별하지 않으므로 중복이 발생함
    # 만약 시간 초과날 경우 이를 제거해 주어야 함

    another_team = []
    for i in range(N):
        if i not in team:
            another_team.append(i)

    difference_ability = abs(cal_ability(team) - cal_ability(another_team))
    # print(difference_ability)
    result = min(result, difference_ability)

print(result)
