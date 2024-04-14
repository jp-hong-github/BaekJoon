n = int(input())
data = list(map(int, input().split()))

result = int(10e9)
result_data = [0, 0]
stop = 0

for i in range(n - 1):
    start = i + 1
    end = n - 1
    result_temp = int(10e9)
    result_data_temp = [0, 0]

    while start <= end:
        mid = (start + end) // 2
        temp = data[mid] + data[i]
        # print('i :',i,' start : ',start,' end : ',end,' mid : ',mid,' temp : ',temp,' result : ',result_data,result)

        if temp == 0:
            result_data[0] = i
            result_data[1] = mid
            stop = 1
            break
        ####################################################
        if abs(temp) < abs(result_temp):
            result_data_temp[0] = i
            result_data_temp[1] = mid
            result_temp = temp
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
    if stop == 1:
        break
    if abs(result) > abs(result_temp):
        result_data[0] = result_data_temp[0]
        result_data[1] = result_data_temp[1]
        result = result_temp


print(data[result_data[0]], data[result_data[1]])
