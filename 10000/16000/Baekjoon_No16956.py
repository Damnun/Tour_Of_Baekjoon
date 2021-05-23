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

"""
BFS를 이용한 문제.
늑대가 양에게 접근하지 못하는 방법을
BFS로 풀어야 했는데, 울타리를 어디에 두어야 고민한 결과 늑대와 양을 제외하고 전부 울타리로 만들어 버리기로 했다 (울타리의 최소를 구하는게 아님)
"""