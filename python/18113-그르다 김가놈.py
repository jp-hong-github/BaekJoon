import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())

gimbab = []


for _ in range(n):
    temp = int(input())
    if temp >= 2 * k:
        gimbab.append(temp - 2 * k)
    elif 2 * k > temp and temp > k:
        gimbab.append(temp - k)

start = 1
end = int(10e9)
count = 0

# print(gimbab)
answer = 0
while start <= end:
    mid = (start + end) // 2
    # print(start,end,mid)
    for gimbab_ in gimbab:
        count += gimbab_ // mid  # mid == p p를 최대로 해야 함
    if m <= count:
        start = mid + 1
    else:
        end = mid - 1
    # print("count  : ",count)
    count = 0

if end == 0:
    print(-1)
else:
    print(end)
