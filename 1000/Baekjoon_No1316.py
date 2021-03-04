num = int(input())
count = 0

for i in range(num):
    a = input()
    b = set(a)

    for j in b:
        c = set(a[a.index(j):a.count(j)+a.index(j)])
        
        if len(c) == 1:
            result = 1
        else:
            result = 0
            break
    
    if result == 1:
        count += 1

print(count)
