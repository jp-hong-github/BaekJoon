import sys

input = sys.stdin.readline
N, M = map(int, input().split())

given_numbers = list(set(map(int, input().split())))
given_numbers.sort()


def dfs(count, idx, num_list):
    global N, M
    if count == M:
        print(*num_list)
    else:
        for next in range(idx, len(given_numbers)):
            num_list.append(given_numbers[next])
            dfs(count + 1, next, num_list)
            num_list.pop()


dfs(0, 0, [])
