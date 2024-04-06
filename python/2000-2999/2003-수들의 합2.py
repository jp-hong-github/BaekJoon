import sys

input = sys.stdin.readline
N, M = map(int, input().split())

num_list = list(map(int, input().split()))


def check(temp):
    global M, result
    if temp == M:
        result += 1
        return True
    elif temp > M:
        return True
    else:
        return False


result = 0
for i in range(N):
    temp = num_list[i]
    if not check(temp):
        for k in range(i + 1, N):
            temp += num_list[k]
            if check(temp):
                break
print(result)
