"""
               [2]
               WWW
               WWW
               WWW
          [3]  [0]  [4]  [5]
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
               [1]
               YYY
               YYY
               YYY
"""


def rotate(cube, index):
    # 값을 시계방향으로 2번 돌려서 rotate 시킴
    for _ in range(2):
        tmp = cube[index][0][0]
        cube[index][0][0] = cube[index][1][0]
        cube[index][1][0] = cube[index][2][0]
        cube[index][2][0] = cube[index][2][1]
        cube[index][2][1] = cube[index][2][2]
        cube[index][2][2] = cube[index][1][2]
        cube[index][1][2] = cube[index][0][2]
        cube[index][0][2] = cube[index][0][1]
        cube[index][0][1] = tmp


def clock(direction):
    count = 1 if direction[1] == '+' else 3
    for _ in range(count):
        solution(cube, direction)


def solution(cube, direction):
    if direction[0] == 'U':
        tmp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = tmp
        rotate(cube, 2)

    elif direction[0] == 'D':
        tmp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = tmp
        rotate(cube, 1)

    elif direction[0] == 'F':
        tmp = cube[2][2]
        cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = tmp
        rotate(cube, 0)

    elif direction[0] == 'B':
        tmp = cube[2][0]
        cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
        cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = tmp
        rotate(cube, 5)

    elif direction[0] == 'L':
        tmp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp
        rotate(cube, 3)

    elif direction[0] == 'R':
        tmp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = tmp
        rotate(cube, 4)


def result(cube):
    for i in range(3):
        for j in range(3):
            print(cube[2][i][j], end='')
        print()


test_case = int(input())
for _ in range(test_case):
    loop_case = int(input())
    colors = ['r', 'y', 'w', 'g', 'b', 'o']
    cube = [[] for _ in range(6)]

    for i in colors:
        for j in range(3):
            cube[colors.index(i)].append([i, i, i])

    data = list(map(str, input().split()))
    for i in data:
        clock(i)
    result(cube)

"""
-는 따로 구현해 줄 필요 없음, +를 3번하면 -가 나옴
https://crackerjacks.tistory.com/19
각 테스트 케이스에 대한 디버깅
함수에 direction을 넣어 solution만 하게끔 바꿔보자

20210620
문제 푸는데 정말 오래 걸렸던 것 같다
사실 기본 방향을 돌려주는건 그냥 단순 시간노동인데
F+ 를 돌렸을 때 정방향의 123456789를 741852963 순으로 시계방향 회전해주는걸
tmp = cube + [] 로 딥카피 하여 일일이 대조했었는데
이렇게되면 기존 cube값과의 충돌로 인해 값이 계속 오류가 났었다.
이를 1씩 오른쪽으로 돌려주는걸 2번 반복하여 해결하였다.
처음 풀어보는 플레티넘 5 // 고난이도 구현문제.
복잡한 연산이 필요 없는 대신 빠른 판단력과 사고력이 필요한 문제이다
사실상 시간싸움이라는 말이 되는데, 이 문제를 푸는데 며칠이 걸렸다는건
내가 아직 많이 멀었다는 증거일 것이다. 더욱 노력하자.
"""
