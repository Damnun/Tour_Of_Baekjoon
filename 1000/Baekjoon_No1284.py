while True:
    n = input()
    if n == '0':
        break
    ans = len(n)+1
    for i in n:
        if i == '0':
            ans += 4 
        elif i == '1':
            ans += 2
        else:
            ans += 3
    print(ans)
