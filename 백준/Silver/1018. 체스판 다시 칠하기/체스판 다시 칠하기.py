import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

# sr = 시작 행, sc = 시작 열
def count_paint(sr, sc):
    b_count = 0  # 좌상단이 B일 때 틀린 칸 수
    w_count = 0  # 좌상단이 W일 때 틀린 칸 수

    for i in range(8):
        # 이 줄의 첫 칸 기대 색
        if i % 2 == 0:  # 짝수 줄
            b_expect = 'B'
            w_expect = 'W'
        else:           # 홀수 줄
            b_expect = 'W'
            w_expect = 'B'

        for j in range(8):
            cur = board[sr + i][sc + j]  # 현재 칸 색

            if cur != b_expect:
                b_count += 1
            if cur != w_expect:
                w_count += 1

            # 옆으로 갈 때 색 반전
            b_expect = 'W' if b_expect == 'B' else 'B'
            w_expect = 'B' if w_expect == 'W' else 'W'

    return b_count if b_count < w_count else w_count


# 전체 탐색
min_count = 64  # 최악: 전부 칠함
for sr in range(n - 7):
    for sc in range(m - 7):
        repaint = count_paint(sr, sc)
        if repaint < min_count:
            min_count = repaint

print(min_count)
