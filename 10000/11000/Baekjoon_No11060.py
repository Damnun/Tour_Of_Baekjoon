n = int(input())
a = list(map(int, input().split()))
d = [0] + ([-1] * n)
# d[i] = 가능한 모든 d[j]중 최소값 + 1

for i in range(1, n):
    for j in range(i):
        if d[j] != -1 and i - j <= a[j]:
            if d[i] == -1 or d[i] > d[j] + 1:
                d[i] = d[j] + 1
print(d[n - 1])
