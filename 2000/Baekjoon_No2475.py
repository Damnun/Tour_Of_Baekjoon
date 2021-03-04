num = input().split(" ")
result = 0
for i in num:
    tmp = int(i)
    if tmp == 0:
        continue
    result += tmp*tmp
print(result%10)