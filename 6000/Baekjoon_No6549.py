import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    n = data.pop(0)
    answer = 0
    s = []

    if n == 0:
        break

    for i in range(n):
        while s and data[s[-1]] > data[i]:
            height = data[s.pop()]

            if s:
                width = i - s[-1] - 1
            else:
                width = i
            answer = max(answer, width * height)
        s.append(i)

    while s:
        height = data[s.pop()]

        if s:
            width = n - s[-1] - 1
        else:
            width = n
        answer = max(answer, width * height)
    print(answer)
