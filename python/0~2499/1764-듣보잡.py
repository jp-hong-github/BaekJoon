import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

no_listen = []
no_see = []
# no_listen_and_see = []

for _ in range(N):
    no_listen.append(input())

for _ in range(M):
    no_see.append(input())
    # if no_see_person in no_listen:
    #     heapq.heappush(no_listen_and_see, no_see_person)
    #     no_listen.remove(no_see_person)

no_listen_and_see = list(set(no_listen) & set(no_see))
no_listen_and_see.sort()

print(len(no_listen_and_see))
for case in no_listen_and_see:
    print(case, end="")
