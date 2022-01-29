n = 9
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * 10 for _ in range(n)] # 행의 스도쿠 판별
c2 = [[False] * 10 for _ in range(n)] # 열의 스도쿠 판별
c3 = [[False] * 10 for _ in range(n)] # 3*3 작은 사각형의 스도쿠 판별


def square(x, y):
    return (x // 3) * 3 + (y // 3)  # 3*3 작은 사각형을 3 * 3 사각형으로 봤을 때 row-major-order로 나타낼 수 있음

def go(z):  # 빈 칸을 채우는 방법
    if z == 81:  # 마지막 칸 까지 다 채우면 정답
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // n
    y = z % n
    if a[x][y] != 0: # 스도쿠의 해당 칸이 이미 차있다면 다음 칸으로 이동
        return go(z + 1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                a[x][y] = i
                if go(z + 1):
                    return True
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = False
        return False


for i in range(n):
    for j in range(n):
        if a[i][j] != 0:  # 만약 빈칸이 아니라면 (값이 있다면)
            c[i][a[i][j]] = True  # 행에 값이 있음
            c2[j][a[i][j]] = True  # 열에 값이 있음
            c3[square(i, j)][a[i][j]] = True  # 33사각형에 값이 있음
go(0)
