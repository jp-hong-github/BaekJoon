import sys
from collections import deque

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    students_graph = [0] + list(map(int, input().split()))
    result = n
    visited = [False for _ in range(1 + n)]

    for i in range(1, len(students_graph)):
        # 이미 한 번 본 학생은 통과
        if visited[i] is True:
            continue

        cycle = []
        original_student = i
        current_student = original_student
        while True:
            # 방문한 경우
            if visited[current_student]:
                # 사이클에 해당 학생이 포함되는 경우
                if current_student in cycle:
                    result -= len(cycle[cycle.index(current_student) :])
                break

            visited[current_student] = True
            cycle.append(current_student)
            current_student = students_graph[current_student]

    print(result)
