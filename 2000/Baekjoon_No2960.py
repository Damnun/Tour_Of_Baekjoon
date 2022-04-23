n, k = map(int, input().split())
ans = 0

data = [True] * (n + 1)
for i in range(2, len(data) + 1):
    for j in range(i, n + 1, i):
        if data[j] == True:
            data[j] = False
            ans += 1
            if ans == k:
                print(j)
                break
