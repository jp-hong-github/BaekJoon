import sys

input = sys.stdin.readline

# 입력 받기
tree_num, slice_cost, money_per_slice = map(int, input().split())
tree_list = [int(input()) for _ in range(tree_num)]

result = 0
for slice_size in range(1, max(tree_list) + 1):
    temp_result = 0
    for tree in tree_list:
        tree_slice_count, tree_remain = divmod(tree, slice_size)

        if tree_remain > 0:
            cost = tree_slice_count * slice_cost
        else:
            cost = (tree_slice_count - 1) * slice_cost

        profit = tree_slice_count * money_per_slice * slice_size - cost
        if profit > 0:
            temp_result += profit

    result = max(result, temp_result)

print(result)
