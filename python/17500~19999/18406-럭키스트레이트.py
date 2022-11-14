data = input()

left = data[:len(data)//2]
right = data[len(data)//2:]

leftsum=0
rightsum=0
for i in range(len(left)):
    leftsum += int(left[i])
    rightsum += int(right[i])
    
if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")