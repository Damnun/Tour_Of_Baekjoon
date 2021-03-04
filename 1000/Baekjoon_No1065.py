num = int(input())
cnt = 0
ans = []

for i in range(num+1):
    if i == 0:
        continue

    elif i == 1000:
        break

    elif i > 0 and i < 100:
        cnt += 1

    elif i >= 100 and i < 1000:
        #print(int(i/100), int(i%100/10), int(i%100%10))
        ans.append(int(i/100))
        ans.append(int(i % 100/10))
        ans.append(int(i % 100 % 10))
        if (ans[1] - ans[0]) == (ans[2] - ans[1]):
            cnt += 1
        ans = []

print(cnt)
