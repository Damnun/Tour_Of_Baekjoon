amount = int(input())
road_length = list(map(int, input().split()))
road_length_sum = sum(road_length)
oil_price = list(map(int, input().split()))
result = 0

del(oil_price[len(oil_price)-1])
min_price = oil_price[0]
result = oil_price[0] * road_length[0]
for i in range(1, amount-1):
    if oil_price[i] > min_price:
        result += min_price * road_length[i]
    else:
        result += oil_price[i] * road_length[i]
        min_price = oil_price[i]
print(result)
