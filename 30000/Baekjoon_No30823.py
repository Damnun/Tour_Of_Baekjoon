n, k = map(int, input().split())
data = input()

if k == 1:
    ans = data
elif (n - k) % 2:
    ans = data[k - 1:] + data[:k - 1]
else:
    ans = data[k - 1:] + data[k - 2:: -1]

print(ans)
