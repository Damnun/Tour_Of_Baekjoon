a, b = map(int, input().split())
c = input().split()


for i in range(a):
    if int(c[i]) < b:
        print(int(c[i]), end=' ')

num = 3
print(f"{num}", num)
