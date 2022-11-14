T = int(input())
func_list = []
arr_list = []

import re

for i in range(T):
    func_list.append(input().split())
    a = input()
    temp = input()
    arr_list.append(int(re.sub("\[|\]|,","",temp)))
    
print(arr_list)

'''
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
'''