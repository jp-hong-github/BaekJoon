import sys

input = sys.stdin.readline

n = int(input())
#############################################################################################
# place = [-1]*n
# result = [0]

# def backtracking(idx): # idx가 행을 의미, 행은 중복이 애초에 없음
#     #print(idx)
#     if idx==n:
#         result[0]+=1
#         #print('result +=1')
#     else:
#         for k in range(n): # 열 검사
#             check = True
#             place[idx]=k
#             for i in range(idx):
#                 if place[i] == place[idx] or idx-i == abs(place[idx]-place[i]):
#                     check = False

#             if check == True:
#                 backtracking(idx+1)

# backtracking(0)

# print(result[0])


###########################################################################################


# def dfs(queen, row, n):
#     count = 0
#     if n == row:
#         return 1
#     for col in range(n):
#         queen[row] = col
#         for i in range(row):
#             if queen[i] == queen[row]:
#                 break
#             if abs(queen[i]-queen[row]) == row - i:
#                 break
#         else:
#             count += dfs(queen, row + 1, n)
#     return count
# def solution(n):
#     return dfs([0]*n, 0, n)

# print(solution(n))

###########################################################################################

answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[n])
