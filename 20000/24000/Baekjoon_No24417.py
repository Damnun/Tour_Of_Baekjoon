a = b = 1
n = int(input())
for i in range(3, n + 1):
    c = (a + b) % 1000000007
    a = b
    b = c
print(c, n - 2)
