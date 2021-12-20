n = int(input())
for i in range(n):
    data = list(input().split(' '))
    print("Case #" + str(i + 1) +": ", end = '')
    for j in data[::-1]:
        print(j, end=' ')
    print()
