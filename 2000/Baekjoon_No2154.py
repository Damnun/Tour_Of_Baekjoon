data = ""
n = int(input())
for i in range(1, n + 1):
    data += str(i)

print(data.index(str(n)) + 1)
