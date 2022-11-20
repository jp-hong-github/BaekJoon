n = int(input())
lst = list(map(int, input().split()))
lst.sort()


r = []
for i in range(len(lst) - 1):
    for k in range(i + 1, len(lst)):
        r.append(lst[k] - lst[i])

print(r)
