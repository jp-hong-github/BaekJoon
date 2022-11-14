import sys
input = sys.stdin.readline

n = int(input())


print(((1/(5**(1/2)))*(((1+(5**(1/2)))/2)**n) - (((1-(5**(1/2)))/2)**n) )%1000000007)