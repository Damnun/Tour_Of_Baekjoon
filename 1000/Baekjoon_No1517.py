import sys
input = sys.stdin.readline


def solution(s, e):
    global result, data

    if s < e:
        m = (s + e) // 2
        solution(s, m)
        solution(m + 1, e)

        f, b = s, m + 1
        tmp = []

        while f <= m and b <= e:
            if data[f] <= data[b]:
                tmp.append(data[f])
                f += 1
            else:
                tmp.append(data[b])
                b += 1
                result += m - f + 1

        if f <= m:
            tmp += data[f : m + 1]
        if b <= e:
            tmp += data[b : e + 1]

        for i in range(len(tmp)):
            data[s + i] = tmp[i]


n = int(input())
data = list(map(int, input().split()))
result = 0
solution(0, n - 1)
print(result)


