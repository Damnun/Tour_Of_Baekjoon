n = int(input())
a = {}

for i in range(n) :
    cur = int(input())
    if cur in a :
        a[cur] += 1
    else :
        a[cur] = 1

res = sorted(a.items(), key = lambda x : (-x[1],x[0]))
print(res[0][0])
