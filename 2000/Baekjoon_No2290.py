import sys
print = sys.stdout.write

# 각 LCD 판의 모양을 미리 만들어두기
c = (
    (1, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 0, 1, 0),
    (1, 0, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (0, 1, 1, 1, 0, 1, 0),
    (1, 1, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 1, 1, 1),
    (1, 0, 1, 0, 0, 1, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1)
)

s, n = input().split()
s, m = int(s), len(n) # m에 n의 길이 저장

for i in range(5):
    if i in [0, 2, 4]: # 가로 --에 대한 처리
        for j in range(m):
            now = int(n[j])
            if j != 0:
                print(' ')
            print(' ')
            if (i == 0 and c[now][0]) or (i == 2 and c[now][3]) or (i == 4 and c[now][6]):
                print('-'*s)
            else:
                print(' '*s)
            print(' ')
        print('\n')
    else: # 세로 ㅣㅣ에 대한 처리
        for l in range(s):
            for j in range(m):
                now = int(n[j])
                if j != 0:
                    print(' ')
                if (i == 1 and c[now][1]) or (i == 3 and c[now][4]):
                    print('|')
                else:
                    print (' ')
                print(' '*s)
                if (i == 1 and c[now][2]) or (i == 3 and c[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')
