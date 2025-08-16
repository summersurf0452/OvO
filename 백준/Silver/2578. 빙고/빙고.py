#8/16

import sys


# 빙고판(5x5) 입력 받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 숫자 25개 (5줄을 이어붙여 1차원 리스트로)
calls = []
for _ in range(5):
    calls.extend(map(int, sys.stdin.readline().split()))


# 표시판  준비

marked = [[False] * 5 for _ in range(5)]  # True면 체크된 칸

#빙고 줄을 세는 함수
def count_bingo(marked):
    count= 0

    # 가로 5줄
    for r in range(5):
        if all(marked[r][c] for c in range(5)):
            count += 1

    # 세로 5줄
    for c in range(5):
        if all(marked[r][c] for r in range(5)):
            count += 1

    # 대각선 2줄
    if all(marked[i][i] for i in range(5)):
        count += 1
    if all(marked[i][4 - i] for i in range(5)):
        count += 1

    return count

# 숫자를 하나씩 부르며 진행

for i, x in enumerate(calls, start=1):  # i = 몇 번째로 불렀는지
    # x가 있는 칸을 찾아서 체크
    for r in range(5):
        for c in range(5):
            if board[r][c] == x:
                marked[r][c] = True

    # 현재까지 완성된 줄 개수 확인
    if count_bingo(marked) >= 3:
        print(i)  # i번째 숫자에서 빙고
        break
