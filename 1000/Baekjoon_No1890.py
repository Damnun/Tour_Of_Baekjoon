n = int(input())
data = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        value = data[i][j]
        down = i + value
        right = j + value

        # 우로 갈 수 있는 경우
        if right < n:
            dp[i][right] += dp[i][j]

        # 하로 갈 수 있는 경우
        if down < n:
            dp[down][j] += dp[i][j]

print(dp[n-1][n-1])

"""
bfs 문제인 줄 알았는데 bfs로 풀게 되면 시간 초과가 나온다
이 경우 Dp로 점화식을 만들거나 테이블을 구성해서 풀어야 한다.
현재 위치에서 우로 갈 수 있는 경우와 하로 갈 수 있는 경우, 2가지 경우를 나누어
dp테이블에 저장해주었다.
"""