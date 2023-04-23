n = int(input())


students = []
for i in range(n):
    name,korean,english,math = list(map(str,input().split()))
    students.append([name,int(korean),int(english),int(math)])
    
result = sorted(students,key = lambda x : (-x[1],x[2],-x[3],x[0]))#다중 정렬

for student in result:
    print(student[0])