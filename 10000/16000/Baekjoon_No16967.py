"""
B[x + 1][y +1] = A[x + 1][y + 1] + A[1][1]
A[1][1] = B[x + 1][y + 1] - A[x + 1][y + 1]
이므로 x, y가 향상 양수임을 이용해 문제를 해결 할 수 있음.
"""
h, w, x, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h + x)]
for i in range(h):
    for j in range(w):
        a[i + x][j + y] -= a[i][j]
for i in range(h):
    print(*a[i][:w])
