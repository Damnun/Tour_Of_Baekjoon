n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n - 1, -1, -1):
    d[i] = 1
    for j in range(i + 1, n):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
print(max(d))

"""
D[i] = a[i]에서 끝나는 가장긴 감소하는 부분수열의 길이
a[0], a[1], a[2].....a[j], a[i]
a[j] > a[i]
d[i] = d[j] + 1
초기값 = 1
"""
