data = int(input())
fibo_a = [0 for _ in range(data + 1)]
fibo_b = [0 for _ in range(data + 1)]

fibo_a[0] = 1
fibo_a[1] = 0
fibo_b[0] = 0
fibo_b[1] = 1

for i in range(2, data + 1):
    fibo_a[i] = fibo_a[i - 1] + fibo_a[i - 2]
    fibo_b[i] = fibo_b[i - 1] + fibo_b[i - 2]

print(fibo_a[data], fibo_b[data])
