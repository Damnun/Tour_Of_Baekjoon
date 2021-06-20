test_case = int(input())
colors = ['w', 'y', 'r', 'o', 'g', 'b']


def solution(data):
    for i in data:
        tmp_cubes = cubes + []
        tmp = []
        if i == 'U+':
            cubes[0][0] = tmp_cubes[0][6]
            cubes[0][1] = tmp_cubes[0][3]
            cubes[0][2] = tmp_cubes[0][0]
            cubes[0][3] = tmp_cubes[0][7]
            cubes[0][4] = tmp_cubes[0][4]
            cubes[0][5] = tmp_cubes[0][1]
            cubes[0][6] = tmp_cubes[0][8]
            cubes[0][7] = tmp_cubes[0][5]
            cubes[0][8] = tmp_cubes[0][2]
            cubes[2][0] = tmp_cubes[5][0]
            cubes[2][1] = tmp_cubes[5][1]
            cubes[2][2] = tmp_cubes[5][2]
            cubes[5][0] = tmp_cubes[3][0]
            cubes[5][1] = tmp_cubes[3][1]
            cubes[5][2] = tmp_cubes[3][2]
            cubes[3][0] = tmp_cubes[4][0]
            cubes[3][1] = tmp_cubes[4][1]
            cubes[3][2] = tmp_cubes[4][2]
            cubes[4][0] = tmp_cubes[2][0]
            cubes[4][1] = tmp_cubes[2][1]
            cubes[4][2] = tmp_cubes[2][2]
        elif i == 'U-':
            tmp.append(cubes[2][0])
            tmp.append(cubes[2][1])
            tmp.append(cubes[2][2])
            cubes[0][0] = tmp_cubes[0][2]
            cubes[0][1] = tmp_cubes[0][5]
            cubes[0][2] = tmp_cubes[0][8]
            cubes[0][3] = tmp_cubes[0][1]
            cubes[0][4] = tmp_cubes[0][4]
            cubes[0][5] = tmp_cubes[0][7]
            cubes[0][6] = tmp_cubes[0][0]
            cubes[0][7] = tmp_cubes[0][3]
            cubes[0][8] = tmp_cubes[0][6]
            cubes[2][0] = cubes[4][0]
            cubes[2][1] = cubes[4][1]
            cubes[2][2] = cubes[4][2]
            cubes[4][0] = cubes[3][0]
            cubes[4][1] = cubes[3][1]
            cubes[4][2] = cubes[3][2]
            cubes[3][0] = cubes[5][0]
            cubes[3][1] = cubes[5][1]
            cubes[3][2] = cubes[5][2]
            cubes[5][0] = tmp[0]
            cubes[5][1] = tmp[1]
            cubes[5][2] = tmp[2]
        elif i == 'D+':
            tmp.append(cubes[2][6])
            tmp.append(cubes[2][7])
            tmp.append(cubes[2][8])
            cubes[1][0] = tmp_cubes[1][6]
            cubes[1][1] = tmp_cubes[1][3]
            cubes[1][2] = tmp_cubes[1][0]
            cubes[1][3] = tmp_cubes[1][7]
            cubes[1][4] = tmp_cubes[1][4]
            cubes[1][5] = tmp_cubes[1][1]
            cubes[1][6] = tmp_cubes[1][8]
            cubes[1][7] = tmp_cubes[1][5]
            cubes[1][8] = tmp_cubes[1][2]
            cubes[2][6] = cubes[4][6]
            cubes[2][7] = cubes[4][7]
            cubes[2][8] = cubes[4][8]
            cubes[4][6] = cubes[3][6]
            cubes[4][7] = cubes[3][7]
            cubes[4][8] = cubes[3][8]
            cubes[3][6] = cubes[5][6]
            cubes[3][7] = cubes[5][7]
            cubes[3][8] = cubes[5][8]
            cubes[5][6] = tmp[0]
            cubes[5][7] = tmp[1]
            cubes[5][8] = tmp[2]
        elif i == 'D-':
            tmp.append(cubes[2][6])
            tmp.append(cubes[2][7])
            tmp.append(cubes[2][8])
            cubes[1][0] = tmp_cubes[1][2]
            cubes[1][1] = tmp_cubes[1][5]
            cubes[1][2] = tmp_cubes[1][8]
            cubes[1][3] = tmp_cubes[1][1]
            cubes[1][4] = tmp_cubes[1][4]
            cubes[1][5] = tmp_cubes[1][7]
            cubes[1][6] = tmp_cubes[1][0]
            cubes[1][7] = tmp_cubes[1][3]
            cubes[1][8] = tmp_cubes[1][6]
            cubes[2][6] = cubes[5][6]
            cubes[2][7] = cubes[5][7]
            cubes[2][8] = cubes[5][8]
            cubes[5][6] = cubes[3][6]
            cubes[5][7] = cubes[3][7]
            cubes[5][8] = cubes[3][8]
            cubes[3][6] = cubes[4][6]
            cubes[3][7] = cubes[4][7]
            cubes[3][8] = cubes[4][8]
            cubes[4][6] = tmp[0]
            cubes[4][7] = tmp[1]
            cubes[4][8] = tmp[2]
        elif i == 'F+':
            tmp.append(cubes[0][2])
            tmp.append(cubes[0][5])
            tmp.append(cubes[0][8])
            cubes[2][0] = tmp_cubes[2][6]
            cubes[2][1] = tmp_cubes[2][3]
            cubes[2][2] = tmp_cubes[2][0]
            cubes[2][3] = tmp_cubes[2][7]
            cubes[2][4] = tmp_cubes[2][4]
            cubes[2][5] = tmp_cubes[2][1]
            cubes[2][6] = tmp_cubes[2][8]
            cubes[2][7] = tmp_cubes[2][5]
            cubes[2][8] = tmp_cubes[2][2]
            cubes[0][2] = cubes[4][2]
            cubes[0][5] = cubes[4][5]
            cubes[0][8] = cubes[4][8]
            cubes[4][2] = cubes[1][2]
            cubes[4][5] = cubes[1][5]
            cubes[4][8] = cubes[1][8]
            cubes[1][2] = cubes[5][0]
            cubes[1][5] = cubes[5][3]
            cubes[1][8] = cubes[5][6]
            cubes[5][0] = tmp[0]
            cubes[5][3] = tmp[1]
            cubes[5][6] = tmp[2]
        elif i == 'F-':
            tmp.append(cubes[0][2])
            tmp.append(cubes[0][5])
            tmp.append(cubes[0][8])
            cubes[2][0] = tmp_cubes[2][2]
            cubes[2][1] = tmp_cubes[2][5]
            cubes[2][2] = tmp_cubes[2][8]
            cubes[2][3] = tmp_cubes[2][1]
            cubes[2][4] = tmp_cubes[2][4]
            cubes[2][5] = tmp_cubes[2][7]
            cubes[2][6] = tmp_cubes[2][0]
            cubes[2][7] = tmp_cubes[2][3]
            cubes[2][8] = tmp_cubes[2][6]
            cubes[0][2] = cubes[5][0]
            cubes[0][5] = cubes[5][3]
            cubes[0][8] = cubes[5][6]
            cubes[5][0] = cubes[1][2]
            cubes[5][3] = cubes[1][5]
            cubes[5][6] = cubes[1][8]
            cubes[1][2] = cubes[4][2]
            cubes[1][5] = cubes[4][5]
            cubes[1][8] = cubes[4][8]
            cubes[4][2] = tmp[0]
            cubes[4][5] = tmp[1]
            cubes[4][8] = tmp[2]
        elif i == 'B+':
            tmp.append(cubes[0][0])
            tmp.append(cubes[0][3])
            tmp.append(cubes[0][6])
            cubes[3][0] = tmp_cubes[3][6]
            cubes[3][1] = tmp_cubes[3][3]
            cubes[3][2] = tmp_cubes[3][0]
            cubes[3][3] = tmp_cubes[3][7]
            cubes[3][4] = tmp_cubes[3][4]
            cubes[3][5] = tmp_cubes[3][1]
            cubes[3][6] = tmp_cubes[3][8]
            cubes[3][7] = tmp_cubes[3][5]
            cubes[3][8] = tmp_cubes[3][2]
            cubes[0][0] = cubes[5][2]
            cubes[0][3] = cubes[5][5]
            cubes[0][6] = cubes[5][8]
            cubes[5][2] = cubes[1][0]
            cubes[5][5] = cubes[1][3]
            cubes[5][8] = cubes[1][6]
            cubes[1][0] = cubes[4][0]
            cubes[1][3] = cubes[4][3]
            cubes[1][6] = cubes[4][6]
            cubes[4][0] = tmp[0]
            cubes[4][3] = tmp[1]
            cubes[4][6] = tmp[2]
        elif i == 'B-':
            tmp.append(cubes[0][0])
            tmp.append(cubes[0][3])
            tmp.append(cubes[0][6])
            cubes[3][0] = tmp_cubes[3][2]
            cubes[3][1] = tmp_cubes[3][5]
            cubes[3][2] = tmp_cubes[3][8]
            cubes[3][3] = tmp_cubes[3][1]
            cubes[3][4] = tmp_cubes[3][4]
            cubes[3][5] = tmp_cubes[3][7]
            cubes[3][6] = tmp_cubes[3][0]
            cubes[3][7] = tmp_cubes[3][3]
            cubes[3][8] = tmp_cubes[3][6]
            cubes[0][0] = cubes[4][0]
            cubes[0][3] = cubes[4][3]
            cubes[0][6] = cubes[4][6]
            cubes[4][0] = cubes[1][0]
            cubes[4][3] = cubes[1][3]
            cubes[4][6] = cubes[1][6]
            cubes[1][0] = cubes[5][2]
            cubes[1][3] = cubes[5][5]
            cubes[1][6] = cubes[5][8]
            cubes[5][2] = tmp[0]
            cubes[5][5] = tmp[1]
            cubes[5][8] = tmp[2]
        elif i == 'L+':
            cubes[4][0] = tmp_cubes[4][6]
            cubes[4][1] = tmp_cubes[4][3]
            cubes[4][2] = tmp_cubes[4][0]
            cubes[4][3] = tmp_cubes[4][7]
            cubes[4][4] = tmp_cubes[4][4]
            cubes[4][5] = tmp_cubes[4][1]
            cubes[4][6] = tmp_cubes[4][8]
            cubes[4][7] = tmp_cubes[4][5]
            cubes[4][8] = tmp_cubes[4][2]
            cubes[0][6] = tmp_cubes[3][2]
            cubes[0][7] = tmp_cubes[3][5]
            cubes[0][8] = tmp_cubes[3][8]
            cubes[3][2] = tmp_cubes[1][0]
            cubes[3][5] = tmp_cubes[1][1]
            cubes[3][8] = tmp_cubes[1][2]
            cubes[1][0] = tmp_cubes[2][0]
            cubes[1][1] = tmp_cubes[2][3]
            cubes[1][2] = tmp_cubes[2][6]
            cubes[2][0] = tmp_cubes[0][6]
            cubes[2][3] = tmp_cubes[0][7]
            cubes[2][6] = tmp_cubes[0][8]
        elif i == 'L-':
            tmp.append(cubes[0][6])
            tmp.append(cubes[0][7])
            tmp.append(cubes[0][8])
            cubes[4][0] = tmp_cubes[4][2]
            cubes[4][1] = tmp_cubes[4][5]
            cubes[4][2] = tmp_cubes[4][8]
            cubes[4][3] = tmp_cubes[4][1]
            cubes[4][4] = tmp_cubes[4][4]
            cubes[4][5] = tmp_cubes[4][7]
            cubes[4][6] = tmp_cubes[4][0]
            cubes[4][7] = tmp_cubes[4][3]
            cubes[4][8] = tmp_cubes[4][6]
            cubes[0][6] = cubes[2][0]
            cubes[0][7] = cubes[2][3]
            cubes[0][8] = cubes[2][6]
            cubes[2][0] = cubes[1][0]
            cubes[2][3] = cubes[1][1]
            cubes[2][6] = cubes[1][2]
            cubes[1][0] = cubes[3][2]
            cubes[1][1] = cubes[3][5]
            cubes[1][2] = cubes[3][8]
            cubes[3][2] = tmp[0]
            cubes[3][5] = tmp[1]
            cubes[3][8] = tmp[2]
        elif i == 'R+':
            tmp.append(cubes[0][0])
            tmp.append(cubes[0][1])
            tmp.append(cubes[0][2])
            cubes[5][0] = tmp_cubes[5][6]
            cubes[5][1] = tmp_cubes[5][3]
            cubes[5][2] = tmp_cubes[5][0]
            cubes[5][3] = tmp_cubes[5][7]
            cubes[5][4] = tmp_cubes[5][4]
            cubes[5][5] = tmp_cubes[5][1]
            cubes[5][6] = tmp_cubes[5][8]
            cubes[5][7] = tmp_cubes[5][5]
            cubes[5][8] = tmp_cubes[5][2]
            cubes[0][0] = cubes[2][2]
            cubes[0][1] = cubes[2][5]
            cubes[0][2] = cubes[2][8]
            cubes[2][2] = cubes[1][6]
            cubes[2][5] = cubes[1][7]
            cubes[2][8] = cubes[1][8]
            cubes[1][6] = cubes[3][0]
            cubes[1][7] = cubes[3][3]
            cubes[1][8] = cubes[3][6]
            cubes[3][0] = tmp[0]
            cubes[3][3] = tmp[1]
            cubes[3][6] = tmp[2]
        elif i == 'R-':
            tmp.append(cubes[0][0])
            tmp.append(cubes[0][1])
            tmp.append(cubes[0][2])
            cubes[5][0] = tmp_cubes[5][2]
            cubes[5][1] = tmp_cubes[5][5]
            cubes[5][2] = tmp_cubes[5][8]
            cubes[5][3] = tmp_cubes[5][1]
            cubes[5][4] = tmp_cubes[5][4]
            cubes[5][5] = tmp_cubes[5][7]
            cubes[5][6] = tmp_cubes[5][0]
            cubes[5][7] = tmp_cubes[5][3]
            cubes[5][8] = tmp_cubes[5][6]
            cubes[0][0] = cubes[3][0]
            cubes[0][1] = cubes[3][3]
            cubes[0][2] = cubes[3][6]
            cubes[3][0] = cubes[1][6]
            cubes[3][3] = cubes[1][7]
            cubes[3][6] = cubes[1][8]
            cubes[1][6] = cubes[2][2]
            cubes[1][7] = cubes[2][5]
            cubes[1][8] = cubes[2][8]
            cubes[2][2] = tmp[0]
            cubes[2][5] = tmp[1]
            cubes[2][8] = tmp[2]


for _ in range(test_case):
    cubes = [[0 for _ in range(9)] for _ in range(6)]
    count = 0
    for i in colors:
        for j in range(9):
            cubes[count][j] = i
        count += 1
    loop_case = int(input())
    data = list(map(str, input().split()))
    
    solution(data)
    print(cubes[0][6]+cubes[0][3]+cubes[0][0])
    print(cubes[0][7]+cubes[0][4]+cubes[0][1])
    print(cubes[0][8]+cubes[0][5]+cubes[0][2])

    print("위")
    print(cubes[0][0], cubes[0][1], cubes[0][2])
    print(cubes[0][3], cubes[0][4], cubes[0][5])
    print(cubes[0][6], cubes[0][7], cubes[0][8])
    print("-----------------------------------")
    print("아래")
    print(cubes[1][0], cubes[1][1], cubes[1][2])
    print(cubes[1][3], cubes[1][4], cubes[1][5])
    print(cubes[1][6], cubes[1][7], cubes[1][8])
    print("-----------------------------------")
    print("앞")
    print(cubes[2][0], cubes[2][1], cubes[2][2])
    print(cubes[2][3], cubes[2][4], cubes[2][5])
    print(cubes[2][6], cubes[2][7], cubes[2][8])
    print("-----------------------------------")
    print("뒷")
    print(cubes[3][0], cubes[3][1], cubes[3][2])
    print(cubes[3][3], cubes[3][4], cubes[3][5])
    print(cubes[3][6], cubes[3][7], cubes[3][8])
    print("-----------------------------------")
    print("왼")
    print(cubes[4][0], cubes[4][1], cubes[4][2])
    print(cubes[4][3], cubes[4][4], cubes[4][5])
    print(cubes[4][6], cubes[4][7], cubes[4][8])
    print("-----------------------------------")
    print("오")
    print(cubes[5][0], cubes[5][1], cubes[5][2])
    print(cubes[5][3], cubes[5][4], cubes[5][5])
    print(cubes[5][6], cubes[5][7], cubes[5][8])
    print("-----------------------------------")


"""
0 > 3
3 > 1
1 > 2
2 > 0



큐브는 6가지 면으로 구성
0 / 윗면 / 흰색
1 / 아랫면 / 노란색
2 / 앞면 / 빨간색
3 / 뒷면 / 오렌지색
4 / 왼쪽면 / 초록색
5 / 오른쪽면 / 파란색
으로 가정하고 코딩하였음
U- D- L+ R+
"""

"""
-는 따로 구현해 줄 필요 없음, +를 3번하면 -가 나옴
https://crackerjacks.tistory.com/19
각 테스트 케이스에 대한 디버깅
함수에 direction을 넣어 move만 하게끔 바꿔보자

"""
