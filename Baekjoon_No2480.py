a = input().split(" ")
result = 0
for i in a:
    if a.count(i) == 3:
        result = 10000 + 1000 * int(i)
        break
    elif a.count(i) == 2:
        result = 1000 + 100 * int(i)
        break
    else:
        result = 100 * int(max(a))
print(result)