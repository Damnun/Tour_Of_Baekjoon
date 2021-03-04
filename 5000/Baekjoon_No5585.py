cost = 1000 - int(input())
lista = [500, 100, 50, 10, 5, 1]
count = 0
for i in lista:
    count += cost // i
    cost = cost % i
print(count)
    