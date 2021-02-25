data = int(input())
count = 0
for i in range(1, 10000001):

    tmp = str(i)
    if tmp.count('666') >= 1:
        count += 1
    if count == data:
        print(i)
        break