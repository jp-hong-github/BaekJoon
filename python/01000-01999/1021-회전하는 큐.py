import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = deque(list(map(int, input().split())))

# 각각 두 번째, 세 번째 연산의 횟수를 저장할 변수
second_operation_count = 0
third_operation_count = 0

q = deque([i for i in range(1, N + 1)])

while numbers:
    # 첫 번째 연산을 수행
    if q[0] == numbers[0]:
        q.popleft()
        numbers.popleft()

    # 두 번째 연산을 수행
    elif q.index(numbers[0]) <= len(q) // 2:
        q.rotate(-1)
        second_operation_count += 1

    # 세 번째 연산을 수행
    elif q.index(numbers[0]) > len(q) // 2:
        q.rotate(1)
        third_operation_count += 1


print(second_operation_count + third_operation_count)
