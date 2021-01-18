a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
result = 0

for i in a:
    if i in b:
        print(b.count(i))
        result += b.count(i)

result = len(b) - result
print(result)
