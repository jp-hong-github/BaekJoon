import sys

input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
result = [0] + [-1 for _ in range(N)]

if N == 1:
    print(-1)
else:
    # 스택에는 인덱스를 저장
    stack = []

    for i in range(1, N + 1):
        while True:
            if not stack:
                stack.append(i)
                break
            else:
                if numbers[stack[-1]] < numbers[i]:
                    idx = stack.pop()
                    result[idx] = numbers[i]
                else:
                    stack.append(i)
                    break

    # 스택에 남아 있는 경우는 오큰수가 없는 경우임
    # for i in range(len(stack)):
    # result[stack[i]] = -1

    print(*result[1:])
