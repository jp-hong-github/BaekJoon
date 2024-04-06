import sys

input = sys.stdin.readline

N = int(input())
work_list = []
min_start_time = int(10e9)

for _ in range(N):
    s, t = map(int, input().split())
    min_start_time_temp = t - s
    min_start_time = min(min_start_time, min_start_time_temp)
    work_list.append([s, t])

work_list.sort(key=lambda x: [x[1], x[0]])

result = -1
for time in range(min_start_time, -1, -1):
    flag = False
    time_temp = time
    # print(f'time : {time}')
    for i in range(len(work_list)):
        s, t = work_list[i]
        work_end_time = time + s
        if work_end_time <= t:
            time = work_end_time
        else:
            break

        if i == len(work_list) - 1:
            flag = True

    if flag:
        result = time_temp
        break

print(result)
