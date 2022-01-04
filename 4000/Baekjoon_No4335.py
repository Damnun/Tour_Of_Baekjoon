check = [True] * (10 + 1)
while True:
    n = int(input())
    if n == 0:
        break
    data = input()

    if data == 'too high':
        for i in range(n, 11):
            check[i]=False

    elif data == 'too low':
        for i in range(0, n+1):
            check[i]=False

    else:
        if check[n]:
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        check = [True] * (10 + 1)
