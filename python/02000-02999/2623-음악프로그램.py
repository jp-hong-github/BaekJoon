import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n, m = list(map(int, input().split()))

# 위상 정렬
singers = defaultdict(list)
in_degree = [-1] + [0 for _ in range(n)]

for _ in range(m):
    singer_list = list(map(int, input().split()))[1:]
    for singer_idx in range(len(singer_list) - 1):
        singers[singer_list[singer_idx]].append(singer_list[singer_idx + 1])
        in_degree[singer_list[singer_idx + 1]] += 1


# in degree==0인(가장 앞에 올 수 있는) 원소로 큐를 생성
q = deque(
    [
        singer
        for singer, singer_in_degree in enumerate(in_degree)
        if singer_in_degree == 0
    ]
)


sorted_singers = []

while q:
    current_singer = q.popleft()
    sorted_singers.append(current_singer)

    for next_singer in singers[current_singer]:
        if in_degree[next_singer] > 0:
            in_degree[next_singer] -= 1
            if in_degree[next_singer] == 0:
                q.append(next_singer)

if len(sorted_singers) == n:
    for s in sorted_singers:
        print(s)
else:
    print(0)
