import sys

input = sys.stdin.readline

N = int(input())
tops: list = list(map(int, input().split()))
tops.reverse()
result = [0 for _ in range(N)]

# 스택을 사용
stack = []
for i in range(N):
    if not stack:
        stack.append(i)
    else:
        while True:
            if stack and tops[stack[-1]] < tops[i]:
                result[N - 1 - stack[-1]] = N - i
                stack.pop()
            else:
                stack.append(i)
                break

print(*result)
