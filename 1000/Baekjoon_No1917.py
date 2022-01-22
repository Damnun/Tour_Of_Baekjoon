"""
가능한 모든 전개도 11가지를 미리 입력해 비교하는 방식
각 모양마다 대칭 2회, 회전 4회를 해 비교해주어야 함.
"""

cubes = [
    ["0010",
     "1111",
     "0010"],
    ["0100",
     "1111",
     "1000"],
    ["0010",
     "1111",
     "0100"],
    ["0001",
     "1111",
     "1000"],
    ["0001",
     "1111",
     "0100"],
    ["11100",
     "00111"],
    ["1100",
     "0111",
     "0010"],
    ["1100",
     "0111",
     "0001"],
    ["0010",
     "1110",
     "0011"],
    ["0001",
     "1111",
     "0001"],
    ["1100",
     "0110",
     "0011"]
]

def mirror(b): # 대칭
    ans = []
    for i in range(len(b)):
        temp = b[i][::-1]
        ans.append(temp)
    return ans

def rotate(b): # 회전
    ans = [''] * len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans

def check(a, b, x, y):
    n = len(a)
    for i in range(len(b)):
        for j in range(len(b[0])):
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < n:
                    if b[i][j] == '0':
                        if a[nx][ny] == 1:
                            return False
                    elif b[i][j] == '1':
                        if a[nx][ny] == 0:
                            return False
                else:
                    return False
    return True

t = 3 # 3번의 입력 데이터
for _ in range(t):
    n = 6 # 각각의 입력 데이터는 6개의 줄
    a = [] # 입력을 저장할 리스트
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = False
    for c in cubes:
        cube = [row[:] for row in c]
        for mir in range(2):  # 대칭 2회
            for rot in range(4):  # 회전 4회
                for i in range(n):
                    for j in range(n):  # i, j
                        ans |= check(a, cube, i, j)
                cube = rotate(cube)
            cube = mirror(cube)
    print("yes" if ans else "no")
