import sys; input = sys.stdin.readline

for test in range(int(input())):
    M = int(input())
    a = []
    for i in range(M//10+1):
        a.extend(list(map(int, input().split())))

    print(M//2+1)
    print(a[0], end=" ")
    if M != 1:
        cnt = 1
        for i in range(2, M, 2):
            print(sorted(a[:i + 1])[(i + 1) // 2], end=" ")
            cnt += 1
            if cnt == 10:
                print()
                cnt = 0
        else:
            print()
