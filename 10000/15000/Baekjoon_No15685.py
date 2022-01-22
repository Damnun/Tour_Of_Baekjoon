"""
문제풀이 순서
1. 드래곤 커브 만들기
2. 꼭지점 여부 확인

드래곤 커브 만들기
1. 기존 세대의 방향을 반대로 (배열 순서)
2. 1을 모두 반시계 방향으로 90도 이동
3. 2를 앞번 배열의 뒤에 이어주기

c[i][j], (i,j)가 드래곤 커브의 꼭지점이면 True / False
"""

c = [[False] * 101 for _ in range(101)]  # i, j가 드래곤 커브의 꼭짓점인지 여부
# 우 상 좌 하 direction
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def curve(x, y, dir, gen):  # x좌표, y좌표, 방향, 세대
    ans = [dir]
    for g in range(1, gen + 1):
        temp = ans[:]
        temp = temp[::-1] # 1. 기존 커브를 순서를 뒤집어줌
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 4  # 반시계로 90도 뒤집음
        ans += temp
    return ans

n = int(input())
for _ in range(n):
    y, x, dir, gen = map(int, input().split())
    dirs = curve(x, y, dir, gen)
    c[x][y] = True
    for d in dirs:
        x += dx[d]
        y += dy[d]
        c[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if c[i][j] and c[i][j + 1] and c[i + 1][j] and c[i + 1][j + 1]: # 네 꼭지점이 모두 드래곤 커브이면
            ans += 1
print(ans)
