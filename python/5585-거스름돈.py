num = int(input())

answer = 0
num = 1000-num
answer += num//500
num = num%500

answer += num//100
num = num%100

answer += num//50
num = num%50

answer += num//10
num = num%10

answer += num//5
num = num%5

answer += num//1

print(answer)
