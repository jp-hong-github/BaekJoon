
import sys
while True:
    # \n 제거
    line = sys.stdin.readline().rstrip("\n")

    # 아무것도 입력 받지 못했으면 while문 탈출
    if not line:
        break
    
    print(line)