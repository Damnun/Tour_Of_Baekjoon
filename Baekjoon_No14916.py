cost = int(input())
lista = [5, 2]
count = 0

for i in lista:
    if cost <= 1:
        print('-1')
        break
    else:
        count += cost // i
        cost = cost % i
print(count)