import sys

input = sys.stdin.readline
N, M = map(int, input().split())

given_numbers = list(set(map(int, input().split())))
given_numbers.sort()


def dfs(count, num_list):
    global N, M
    if count == M:
        print(*num_list)
    else:
        # check_value = -1
        for next in range(0, len(given_numbers)):
            # if given_numbers[next] != check_value:
            # check_value = given_numbers[next]
            num_list.append(given_numbers[next])
            dfs(count + 1, num_list)
            num_list.pop()


dfs(0, [])
