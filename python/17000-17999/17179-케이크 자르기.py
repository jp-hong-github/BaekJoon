import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
S = [int(input()) for i in range(M)]
MIN = min(S[0], L - S[M - 1])
for i in range(1, M):
    MIN = min(MIN, S[i] - S[i - 1])
MAX = 0
for i in range(M):
    MAX = max(MAX, max(S[i], L - S[i]))
MAX += 1
Q = [int(input()) for i in range(N)]


def f(x, q):
    i = 0
    prev = 0
    while i < M and q:
        if S[i] - prev >= x:
            prev = S[i]
            q -= 1
        i += 1
    return q == 0 and L - prev >= x


for q in Q:
    lo = MIN
    hi = MAX
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f(mid, q):
            lo = mid
        else:
            hi = mid
    print(lo)
