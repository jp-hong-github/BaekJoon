import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
if len(scv) == 1:
    scv.append(0)
    scv.append(0)
elif len(scv) == 2:
    scv.append(0)

attack_case = [[[float("inf") for _ in range(61)] for _ in range(61)] for _ in range(61)]
attack_case[0][0][0] = 0

for a in range(61):
    for b in range(61):
        for c in range(61):
            if a == b == c == 0:
                continue
            for x, y, z in permutations((a, b, c), 3):
                n_x = max(0, x - 9)
                n_y = max(0, y - 3)
                n_z = max(0, z - 1)
                attack_case[a][b][c] = min(attack_case[a][b][c], attack_case[x][y][z], attack_case[n_x][n_y][n_z] + 1)
                attack_case[x][y][z] = min(attack_case[a][b][c], attack_case[x][y][z], attack_case[n_x][n_y][n_z] + 1)

print(attack_case[scv[0]][scv[1]][scv[2]])

# ! 그리디 알고리즘으로 해결 불가
# =================================================================== #
# def attack_scv(scv):
#     scv_count = len(scv)
#     if scv_count == 1:
#         if scv[0] % 9 == 0:
#             return scv[0] // 9
#         else:
#             return scv[0] // 9 + 1

#     elif scv_count == 2:
#         result = 0
#         while True:
#             scv.sort(reverse=True)
#             while True:
#                 if scv[-1] <= 0:
#                     scv.pop()
#                 else:
#                     break
#             if len(scv) == 0:
#                 return result
#             elif len(scv) == 1:
#                 return result + attack_scv(scv)
#             else:
#                 result += 1
#                 scv[0] -= 9
#                 scv[1] -= 3

#     else:
#         result = 0
#         while True:
#             scv.sort(reverse=True)
#             while True:
#                 if len(scv) > 0 and scv[-1] <= 0:
#                     scv.pop()
#                 else:
#                     break
#             if len(scv) == 0:
#                 return result
#             elif len(scv) == 1:
#                 return result + attack_scv(scv)
#             elif len(scv) == 2:
#                 return result + attack_scv(scv)
#             else:
#                 result += 1
#                 scv[0] -= 9
#                 scv[1] -= 3
#                 scv[2] -= 1


# print(attack_scv(scv))
# =================================================================== #
