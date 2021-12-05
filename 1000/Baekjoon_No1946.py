import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = []
    count = 1
    for _ in range(n):
        data.append(list(map(int, input().split())))
    data.sort()

    tmp = data[0][1]

    for i in range(1, n):
        if tmp > data[i][1]:
            count += 1
            tmp = data[i][1]
    print(count)
