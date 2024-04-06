import sys

input = sys.stdin.readline

m = int(input())
# ! 계산한 것만 출력하면 되므로 수열(리스트) 자체가 필요없음
# arr = [0]

# 쿼리1과 쿼리2에서 미리 쿼리3과 쿼리4의 답을 계산
query_3_answer = 0
query_4_answer = 0
result: list = []

for _ in range(m):
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        query = temp[0]
        if query == 3:  # 쿼리 3
            result.append(query_3_answer)
        elif query == 4:  # 쿼리 4
            result.append(query_4_answer)
    else:
        query, number = temp
        if query == 1:  # 쿼리 1
            # arr.append(number)

            query_3_answer += number
            query_4_answer = query_4_answer ^ number

        elif query == 2:  # 쿼리 2
            # arr.remove(number)

            query_3_answer -= number
            query_4_answer = query_4_answer ^ number  # XOR의 역 계산은 XOR 그 자체

for r in result:
    print(r)
