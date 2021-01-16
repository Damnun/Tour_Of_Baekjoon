a = input()
a = a.lower()

tmp = -1
for i in a:
    if a.count(i) > tmp:
        tmp = a.count(i)
        ans = i
    elif a.count(i) == tmp and i != ans:
        print("?")
        break

print(ans.upper())
