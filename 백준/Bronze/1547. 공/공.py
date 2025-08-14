#8/14

import sys

#현재 공이 있는 컵의 넘버는 1, 컵을 바꿀 횟수를 입력으로 받는다.
total=int(sys.stdin.readline().strip()) # 횟수 변수를 읽고 소비
current=1

#반복하며 컵의 자리를 교환

for _ in range(total):
    x,y=map(int, sys.stdin.readline().split())
    if current==x:
        current=y
    elif current==y:
        current=x

print(current) #현재 최종적으로 공 위에 있는 컵 번호 출력
