n, m = map(int, input().split())
data = {-1: -1}

for i in range(1, n + 1):
    data[input()] = i

reverse_data = dict(map(reversed, data.items()))
for _ in range(m):
    search = input()
    if search.isdigit():
        print(reverse_data[int(search)])
    else:
        print(data[search])
