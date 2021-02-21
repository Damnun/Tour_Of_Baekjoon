data_count = int(input())
data = list(map(int, input().split()))
natural_num = list(range(2,1001))
count = 0

for i in range(2, int(1000**0.5)):
    for j in natural_num:
        if j // i == 1:
            pass
        elif j % i == 0:
            natural_num.remove(j)
for k in data:
    if k in natural_num:
        count += 1
print(count)
