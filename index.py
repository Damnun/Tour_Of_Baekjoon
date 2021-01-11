while True:
    a = int(input())
    if 1 <= a and a <= 10000:
        break

result = 0
for i in range(a):
    result += (i+1)

print(result)
