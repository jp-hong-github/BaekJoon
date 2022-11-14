import sys

input = sys.stdin.readline
N, M = map(int, input().split())

given_numbers = list(map(int, input().split()))
given_numbers.sort()
visited = [False] * N


def dfs(count, num_list, idx):
    global N, M
    if count == M:
        print(*num_list)
    else:
        check_value = -1
        for next in range(idx + 1, N):
            if visited[next] == False and given_numbers[next] != check_value:
                check_value = given_numbers[next]
                visited[next] = True
                num_list.append(given_numbers[next])
                dfs(count + 1, num_list, next)
                num_list.pop()
                visited[next] = False


dfs(0, [], -1)

