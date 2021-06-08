n = int(input())


def dfs(maps, count, x, y):
    maps[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if maps[nx][ny] == 1:
                count = dfs(maps, count + 1, nx, ny)
    return count


maps = [list(map(int, list(input()))) for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            ans.append(dfs(maps, 1, i, j))

print(len(ans))  # 총 집의 개수
for i in sorted(ans):  # 각 집의 호수를 오름차순으로 출력
    print(i)

"""
DFS 를 이용한 기본응용문제
1차원으로 주어진 표에서 큰 범위의 집의 개수, 그 집안에 든 호수의 개수를 count해가며 출력하는 문제였음. 1차평면상에서의 이동을 dx,dy를 이용해 나타내는데 2차 3차는 어떻게 나누게 되는지 몹시 궁금하다. 예전에 토마토 문제를 보았을 때 좌절했는데, 열심히 공부해서 풀어봐야지

"""