"""
주사위 면에 가상의 번호를 매김
dice[i] = i번 면에 있는 수
동 서 남 북으로 굴렸을 때 각각 변하는 값과 변하지 않는 값을 파악.
0  1  2  3
"""

dice = [0] * 7
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, x, y, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
for k in move:
    k -= 1
    nx, ny = x + dx[k], y + dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if k == 0:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif k == 1:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif k == 2:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
    x, y = nx, ny
    if a[x][y] == 0:
        a[x][y] = dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] = 0
    print(dice[1])
