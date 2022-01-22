n, k = map(int, input().split())
a = list(map(int, input().split()))
box = [False] * (2*n)  # 박스의 여부
zero = 0  # 내구도가 0인 로봇의 개수
t = 1

while True:
    # 컨베이어 회전
    a = a[-1:] + a[:-1]
    box = box[-1:] + box[:-1]

    if box[n - 1]: # 내려가는 위치에 박스가 있으면 내린다
        box[n - 1] = False

    for i in range(n - 2, -1, -1):
        if box[i]:
            if box[i + 1] == False and a[i + 1] > 0: # 내구도가 남아있고 다음칸이 비어있으면
                box[i + 1] = True  # 다음칸으로 이동
                box[i] = False  # 기존 칸은 빔
                a[i + 1] -= 1  # 내구도 1 감소
                if a[i + 1] == 0:  # 내구도 없으면 zero += 1
                    zero += 1
    if box[n - 1]:
        box[n - 1] = False

    if a[0] > 0:
        box[0] = True
        a[0] -= 1
        if a[0] == 0:
            zero += 1
    if zero >= k:
        print(t)
        break
    t += 1
