import sys

input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))
remove_node = int(input())

child = [[] for _ in range(N)]

for i in range(N):
    if tree[i] == -1:
        pass
    else:
        child[tree[i]].append(i)


def dfs(node):
    for next_node in child[node]:
        dfs(next_node)
    child[node] = None


dfs(remove_node)
if tree[remove_node] != -1:
    child[tree[remove_node]].remove(remove_node)

result = 0
for i in child:
    if i is not None and len(i) == 0:
        result += 1
print(result)


####################################################
# 인터넷에서 돌아다니는 로직
# 이 방식의 장점은 루트 노드에 대해 따로 생각하지 않아도 된다는 점이다.

# import sys

# input = sys.stdin.readline


# def dfs(node):
#     tree[node] = None
#     for i in range(N):
#         if node == tree[i]:
#             dfs(i)


# N = int(input())
# tree = list(map(int, input().split()))
# remove_node = int(input())

# dfs(remove_node)
# result = 0

# for i in range(N):
#     if tree[i] is not None and i not in tree:
#         result += 1

# print(result)
