import sys

input = sys.stdin.readline

k = int(input())
signs = list(map(str, input().split()))

min_result = "9999999999999999"
max_result = "0000000000000000"


def backtracking(l, string, used_number_set, idx):
    global min_result
    global max_result
    if l == k + 1:
        if int(min_result) > int(string):
            min_result = string
        if int(max_result) < int(string):
            max_result = string
    else:
        if idx == 0:
            for i in range(0, 10):
                used_number_set.add(i)
                backtracking(l + 1, string + f"{i}", used_number_set, idx + 1)
                used_number_set.remove(i)
        else:
            for i in range(0, 10):
                if i not in used_number_set:
                    if signs[idx - 1] == "<":
                        if int(string[idx - 1]) < i:
                            used_number_set.add(i)
                            backtracking(l + 1, string + f"{i}", used_number_set, idx + 1)
                            used_number_set.remove(i)
                    else:
                        if int(string[idx - 1]) > i:
                            used_number_set.add(i)
                            backtracking(l + 1, string + f"{i}", used_number_set, idx + 1)
                            used_number_set.remove(i)


backtracking(0, "", set(), 0)
print(max_result)
print(min_result)
