import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = []
parents = [i for i in range(0, n + 1)]


# 재귀 에러 발생
# def find_parent(v):
#     if parents[v] == v:
#         return v
#     else:
#         return find_parent(parents[v])


# 위의 재귀 함수의 경우 RecursionError가 발생하여 반복문으로 변경
# 시간 초과 발생
# def find_parent(v):
#     while True:
#         if parents[v] == v:
#             return v

#         v = parents[v]


def find_parent(v):
    original_v = v
    while True:
        if parents[v] == v:
            # find 과정에서 부모 노드를 업데이트하는 과정 추가
            parents[original_v] = v
            return v

        v = parents[v]


for _ in range(m):
    operation, a, b = map(int, input().split())
    # 유니온 연산
    if operation == 0:
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        if parent_a > parent_b:
            parents[parent_a] = parent_b
        else:
            parents[parent_b] = parent_a
    # 파인드 연산
    else:
        if find_parent(a) == find_parent(b):
            result.append("YES")
        else:
            result.append("NO")

    # print(f"parents : {parents}")


for r in result:
    print(r)
