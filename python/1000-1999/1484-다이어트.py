import sys

input = sys.stdin.readline

# G = current_weight**2 - memory_weight**2
# G = (c + m) * (c - m)

result = []

G = int(input())

# G의 약수 구하기
G_list = []
for i in range(1, G + 1):
    if G % i == 0:
        G_list.append(i)

len_g_list = len(G_list)
for i in range(len_g_list // 2):
    big = G_list[len_g_list - i - 1]
    small = G_list[i]
    if (big + small) % 2 == 0:
        result.append((big + small) // 2)

if result:
    result.sort()
    for r in result:
        print(r)
else:
    print(-1)
