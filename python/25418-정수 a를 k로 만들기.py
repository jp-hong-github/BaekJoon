import sys
from collections import deque

input = sys.stdin.readline

# 정수 입력
A, K = list(map(int, input().split()))

# (현재 값,연산 횟수)
# 1을 더하는 연산
# 2를 곱하는 연산
# 최소 연산인지 확인
result = int(10e9)
q = deque([(A, 0)])
visited = [False] * K

while q:
    current_value, count = q.popleft()
    if current_value == K:
        result = min(result, count)
        continue

    if current_value > K:
        continue

    if visited[current_value] == True:
        continue

    visited[current_value] = True
    q.append((current_value + 1, count + 1))
    q.append((current_value * 2, count + 1))

print(result)
