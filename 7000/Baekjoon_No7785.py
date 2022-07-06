import sys
input = sys.stdin.readline

n = int(input())
a = dict()
for i in range(n):
    x, y = map(str, input().split())
    if y == "enter":
        a[x] = 1
    else:
        del a[x]
        
a = sorted(a.keys(), reverse=True)
for j in a:
    print(j)
        
