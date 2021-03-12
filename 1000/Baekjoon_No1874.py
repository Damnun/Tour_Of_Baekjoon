n = int(input())
data = []  # 데이터가 들어갈 리스트 (스택)
lista = []
result = []

for i in range(n):
    data.append(int(input()))
data = data[::-1]
value = data.pop()

for i in range(1, n+1):
    lista.append(i)
    result.append('+')
    for _ in range(len(lista)):
        if lista[-1] == value:
            lista.pop()
            result.append('-')
            if not data:
                break
            value = data.pop()
        else:
            break

if not data:
    for i in result:
        print(i)
else:
    print("NO")
"""
8
4
3
6
8
7
5
2
1
"""