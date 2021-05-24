win_count = 0

for _ in range(6):
    result = input()
    if result == 'W':
        win_count += 1

if win_count == 0:
    print("-1")
elif 1 <= win_count <= 2:
    print("3")
elif 3 <= win_count <= 4:
    print("2")
elif 5 <= win_count <= 6:
    print("1")
