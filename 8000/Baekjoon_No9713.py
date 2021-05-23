case = int(input())

for _ in range(case):
    number = int(input())
    ans = 0
    for i in range(1, number + 1):
        if i % 2 == 1:
            ans += i
    print(ans)
