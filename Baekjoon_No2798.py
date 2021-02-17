data, max_data = map(int, input().split())
data_list = list(map(int, input().split()))
tmp = 0

i = 0
while i < data:
    j = i+1
    while j < data:
        k = j+1
        while k < data:
            result = data_list[i] + data_list[j] + data_list[k]
            if result <= max_data and result > tmp:
                if result >= tmp:
                    tmp = result
            k += 1
        j += 1
    i += 1
print(tmp)
