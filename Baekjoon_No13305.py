amount = int(input())
road_length = list(map(int, input().split()))
road_length_sum = sum(road_length)
oil_price = list(map(int, input().split()))
result = 0

del(oil_price[len(oil_price)-1])

min_price = min(oil_price)
min_index = oil_price.index(min_price)

if min_index == 0:
    result = min_price * road_length_sum

else:
    for i in range(min_index):
        result += road_length[i] * oil_price[i]
    result += (sum(road_length[min_index:]) * min_price)

print(result)
