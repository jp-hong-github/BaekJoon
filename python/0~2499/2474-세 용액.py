import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

result_1 = 0
result_2 = 0
result_3 = 0
value = 9999999999999999
for fisrt_number_idx in range(0, n - 2):
    for second_number_idx in range(fisrt_number_idx + 1, n - 1):
        start = second_number_idx + 1
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            sum_number = data[fisrt_number_idx] + data[second_number_idx] + data[mid]
            # print(
            #     "1번 값 : %3d, 2번 값: %3d, 3번 값: %3d, 합 : %3d, result : %3d"
            #     % (
            #         data[fisrt_number_idx],
            #         data[second_number_idx],
            #         data[mid],
            #         sum_number,
            #         value,
            #     )
            # )
            abs_sum_number = abs(sum_number)
            if abs_sum_number < abs(value):
                value = abs_sum_number
                result_1, result_2, result_3 = (
                    data[fisrt_number_idx],
                    data[second_number_idx],
                    data[mid],
                )
                if value == 0:
                    break

            if sum_number > 0:
                end = mid - 1
            else:
                start = mid + 1
            # print("다음 start : %d,다음 end : %d\n" % (start, end))

print(result_1, result_2, result_3)

