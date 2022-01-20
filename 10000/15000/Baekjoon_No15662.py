n = int(input())
a = [list(input()) for _ in range(n)]
k = int(input())


for _ in range(k):
    no, dir = map(int, input().split())  # 회전할 톱니, 방향
    no -= 1
    d = [0] * n
    d[no] = dir

    # 각 톱니가 어떤 방향으로 회전해야 하는지
    # 왼쪽 톱니를 연쇄적으로 구하고
    for i in range(no - 1, -1, -1):
        if a[i][2] != a[i + 1][6]:
            d[i] = -d[i + 1]
        else:
            # 한 톱니가 회전하지 않으면, 그 톱니의 왼쪽 톱니도 회전하지 않는다.
            break

    # 똑같이 오른쪽 톱니
    for i in range(no + 1, n):
        if a[i - 1][2] != a[i][6]:
            d[i] = -d[i - 1]
        else:
            break

    for i in range(n):
        if d[i] == 0:
            continue

        if d[i] == 1: # 시계 방향 회전
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp

        elif d[i] == -1: # 반시계 반향 회전
            temp = a[i][0]
            for j in range(0, 7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp

ans = 0
for i in range(n):
    if a[i][0] == '1':
        ans += 1
print(ans)
