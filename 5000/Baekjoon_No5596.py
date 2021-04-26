lista = list(map(int, input().split()))
listb = list(map(int, input().split()))
resulta = sum(lista)
resultb = sum(listb)

if resulta == resultb:
    print(resulta)
elif resulta >= resultb:
    print(resulta)
else:
    print(resultb)