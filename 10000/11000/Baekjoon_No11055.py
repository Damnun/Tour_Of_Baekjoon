"""
D[i] = i번까지의 최대 합
a[0], a[1], a[2].....a[j], a[i]
a[j] < a[i]
j < i
d[i] = max(d[j]) + a[i]
초기값 = a[i]
"""
n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    d[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + a[i]:
            d[i] = d[j] + a[i]
print(max(d))
