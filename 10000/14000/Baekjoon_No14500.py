import sys
input = sys.stdin.readline
n, m = map(int, input().split())
score_board = [list(map(int, input().split())) for _ in range(n)]

tetrominos = [
    [(0, 1), (0, 2), (0, 3)],  # 가로 막대기
    [(1, 0), (2, 0), (3, 0)],  # 세로 막대기
    [(0, 1), (1, 0), (1, 1)],  # 네모
    [(1, 0), (2, 0), (2, 1)],  # 긴 ㄴ
    [(1, 0), (2, 0), (2, -1)],  # 긴 ㄴ 대칭 / 5
    [(0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 1), (0, 2), (1, 0)],  # ㄱ 대칭
    [(0, 1), (1, 1), (2, 1)],  # 긴 ㄱ
    [(0, 1), (1, 0), (2, 0)],  # 긴 ㄱ 대칭
    [(0, 1), (0, 2), (-1, 2)],  # ㄴ 대칭 / 10
    [(1, 0), (1, 1), (1, 2)],  # ㄴ
    [(1, 0), (1, 1), (2, 1)],  # 선 ㄹ
    [(1, 0), (1, -1), (2, -1)],  # 선 ㄹ 대칭
    [(0, 1), (1, 0), (1, -1)],  # ㄹ 대칭
    [(0, 1), (1, 1), (1, 2)],  # ㄹ / 15
    [(0, 1), (0, 2), (1, 1)],  # ㅜ
    [(0, 1), (0, 2), (-1, 1)],  # ㅗ
    [(1, 0), (2, 0), (1, -1)],  # ㅓ
    [(1, 0), (2, 0), (1, 1)],  # ㅏ / 19
]

result = 0
for i in range(n):
    for j in range(m):
        for tetromino in tetrominos:
            flag = True
            score = score_board[i][j]
            for nx, ny in tetromino:
                x, y = nx + i, ny + j
                if 0 <= x < n and 0 <= y < m:
                    score += score_board[x][y]
                else:
                    flag = False
                    break
            if flag:
                if score > result:
                    result = score
print(result)
