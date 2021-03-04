count = int(input())

for i in range(count):
    a = input()
    for j in range(len(a)-2):
        print(a[j+2]*int(a[0]), end='')
    print()
