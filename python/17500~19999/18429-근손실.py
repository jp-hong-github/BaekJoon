import sys

input = sys.stdin.readline

N, K = map(int, input().split())
exercise = list(map(int, input().split()))
exercise.insert(0, -1)
visited = [False] * (N + 1)

result = 0


def cal(count, weight, case):
    global N, result, K
    if count == N:
        if weight >= 500:
            result += 1
            # print(*case)
    else:
        for next in range(1, N + 1):
            if visited[next] is False:
                # print("next : %d, weight : %d, case : " % (next, weight), case)
                weight += exercise[next]
                weight -= K
                if weight < 500:
                    # print("fail", weight, case, next)
                    pass
                else:
                    visited[next] = True
                    case.append(next)
                    cal(count + 1, weight, case)
                    visited[next] = False
                    case.pop()
                weight += K
                weight -= exercise[next]


cal(0, 500, [])
print(result)
