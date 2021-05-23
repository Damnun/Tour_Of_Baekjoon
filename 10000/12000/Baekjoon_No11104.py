case = int(input())

for _ in range(case):
    result = input()
    count = 1
    ans = 0

    for i in range(1, len(result) + 1):
        index = len(result) - i
        ans += int(result[index]) * count
        count *= 2
    print(ans)