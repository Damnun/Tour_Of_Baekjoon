"""
RGB 거리, R = 0, G = 1, B = 2 라고 하고
A[i][j] = i번 집이 j번색일 경우 로 가정하자.
1. i의 이웃은 i - 1, i + 1
2. 첫 집과 마지막 집은 이웃이 아니다.
3. 모든 이웃은 다른 색의 집이다.
- 연속하는 집을 같은 색으로 칠할 수 없다.

d[i][0] = min(d[i - 1][1], d[i-1][2]) + a[i][0]
d[i][1] = min(d[i - 1][0], d[i-1][2]) + a[i][1]
d[i][2] = min(d[i - 1][0], d[i-1][1]) + a[i][2]
정답 : min(d[n][0], d[n][1], d[n][2])
"""

n = int(input())
a = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[0, 0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i][2]
print(min(d[n][0], d[n][1], d[n][2]))
