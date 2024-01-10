for i in range(int(input())):
    data = list(map(int, input().split()))
    n = data.pop(0)
    data.sort(reverse=True)

    gap = -1
    for j in range(len(data) - 1):
        if data[j] - data[j + 1] > gap:
            gap = data[j] - data[j + 1]

    print("Class", i + 1)
    print(f"Max {data[0]}, Min {data[-1]}, Largest gap {gap}")
