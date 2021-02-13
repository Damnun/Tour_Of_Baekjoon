x, y, w, h = map(int, input().split())
if w-x > h-y:
    print(h-y)
elif h-y > w-x:
    print(w-x)
else:
    print(w-x)