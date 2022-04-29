n = int(input())

def solution(a):
    res = 0
    for i in a:
        if i.isdigit():
            res += int(i)
    return res

b = []
for i in range(n):
    a = input()
    b.append(a)

b.sort(key = lambda x:(len(x), solution(x), x))
for i in b:
    print(i)
