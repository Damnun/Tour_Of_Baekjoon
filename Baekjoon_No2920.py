num = list(map(int, input().split()))

lista = [8, 7, 6, 5, 4, 3, 2, 1]
listb = sorted(lista)

if num == lista:
    print("descending")
elif num == listb:
    print("ascending")
else:
    print("mixed")
