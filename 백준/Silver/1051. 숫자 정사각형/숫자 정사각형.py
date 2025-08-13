#8/13

import sys
input=sys.stdin.readline

def solve():
    N,M=map(int, input().split())

    arr=[list(input().strip()) for _ in range(N)]

    for k in range(min(N,M)-1,-1,-1): # 내립차순으로, 정사각형 전체크기 결정
        for i in range(0,N-k): # 행 시작 위치
            for j in range(0,M-k): # 열 시작 위치
                if arr[i][j]==arr[i][j+k]==arr[i+k][j]==arr[i+k][j+k]:
                    print((k+1)**2)
                    return

    print(1)

if __name__=="__main__":
    solve()