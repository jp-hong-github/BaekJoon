import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# K == 1인 경우 무조건 2를 출력
if K == 1:
    print(2)
else:

    class BreakIt(Exception):
        pass

    try:
        count = 0
        # K >= 2인 경우 제거되는 값을 카운트하면서 K번째 제거되는 값을 출력
        is_prime = [False, False] + [True] * (N - 1)

        for i in range(2, N + 1):
            if is_prime[i]:
                # 소수인 경우 해당 값을 제거
                count += 1
                # 제거된 값이 K번째 제거되는 값인 경우 해당 값을 출력하고 반복문 종료
                if count == K:
                    print(i)
                    raise BreakIt

                for j in range(i + i, N + 1, i):
                    # 소수의 배수인 경우 해당 값을 제거
                    if is_prime[j]:
                        is_prime[j] = False
                        count += 1

                        # 제거된 값이 K번째 제거되는 값인 경우 해당 값을 출력하고 반복문 종료
                        if count == K:
                            print(j)
                            raise BreakIt
    except BreakIt:
        pass
