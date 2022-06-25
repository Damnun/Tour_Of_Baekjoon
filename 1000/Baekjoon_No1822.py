n = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

res = []
for cur in a:
    if cur not in b:
        res.append(cur)

res.sort()
print(len(res))

if len(res) !=0:
    print(*(res))
