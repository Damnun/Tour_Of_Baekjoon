for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a in [1, 5, 6]:
        print(a)
        continue
    
    result = []
    tmp = 1
    for _ in range(b):
        tmp *= a
        tmp %= 10
        if tmp in result:
            break
        result.append(tmp)
    
    result = result[b % len(result) - 1]
    if result == 0:
        print(10)
    else:
        print(result)
