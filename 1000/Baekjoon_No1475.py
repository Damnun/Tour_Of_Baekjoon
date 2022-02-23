import math
check = [0 for i in range(10)]

for i in list(map(int, input())):
    check[i] += 1

check[6] = math.ceil((check[6] + check[9]) / 2)
print(max(check[:9]))
