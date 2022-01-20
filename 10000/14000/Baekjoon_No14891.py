"""
톱니바퀴의 정보
a[i][j] : i번 톱니의 j번 극
톱니에 임의의 숫자를 시장 ( 0 ~ 7 )

시계방향 회전 : 톱니배열이 오른쪽 한칸이동
시계방향 역회전 : 톱니배열이 왼쪽 한칸이동

1. 조사 (어떤 톱니바퀴가 어디로 돌아갈 것인가)
2. 회전

동시에 무엇인가 일어난다는 시뮬레이션 문제가 많으나
실제로 동시에 해결할 수는 없다. 따라서 일단
어떤 것들이 어떤 조건에 의해 동시에 이루어지는지를 먼저 조사! 해야한다.

"""
n = 4
a = [list(input()) for _ in range(n)]
k = int(input())

for _ in range(k):
    no, dir = map(int,input().split()) # 회전할 톱니, 방향
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
        ans |= (1 << i)
print(ans)
