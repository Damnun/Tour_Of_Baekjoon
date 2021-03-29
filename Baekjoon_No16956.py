r, c = map(int, input().split())
data = [list([i for i in input()]) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
flag = False

for i in range(r):
    for j in range(c):
        # 늑대일 경우
        if data[i][j] == 'W':
            for z in range(4):
                nx, ny = i + dx[z], j + dy[z]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                # 양과 늑대가 인접할 경우
                if data[nx][ny] == 'S':
                    flag = True
                    break
        elif data[i][j] == 'S':
            continue
        else:
            data[i][j] = 'D'

if flag:
    print(0)
else:
    print(1)
    for i in data:
        print(''.join(i))
