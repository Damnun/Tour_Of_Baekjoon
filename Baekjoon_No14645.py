station_amount, human = map(int, input().split())
for i in range(station_amount):
    new_human, delete_human = map(int, input().split())
    human = human + new_human - delete_human
print("비와이")
