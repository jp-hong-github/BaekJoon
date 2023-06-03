import sys

input = sys.stdin.readline

n = int(input())

# scores가 전체 점수의 내림차순 리스트라고 하면
# scores[k] >= scores[i] + i - N 이면 1등 가능
# 이 떄 k는 scores의 임의의 인덱스이고 i는 i<k인 임의의 인덱스임
# scores는 앞에 더미 데이터가 있다고 가정하여 인덱스의 범위는 1~N임
scores = [int(input()) for _ in range(n)]
scores.sort(reverse=True)
scores = [0] + scores

max_score = 0
result = 0
for i, v in enumerate(scores):
    if i == 0:
        continue
    elif i == 1:
        result += 1
        max_score = v + i - n
    elif v >= max_score:
        result += 1
        max_score = max(max_score, v + i - n)
    else:
        break

print(result)
