a = list(str(input()))
ans = 0

for i in range(len(a)):
    if i == 0:
        ans += 10
    elif a[i] == a[i - 1]:
        ans += 5
    else:
        ans += 10
print(ans)
