n = int(input()) - 1

cur = 1
for i in range(n, 1, -2):
    cur = cur * i

print(cur % (1000000000 + 7))
