n, k = map(int, input().split())
room_list = dict()

for _ in range(n):
    room_list[input()] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(k):
    name, start, end = input().split()
    for i in range(int(start), int(end)):
        room_list[name][i] = 0

name_list = list(room_list.keys())
name_list.sort()

for j in range(len(name_list)):
    name = name_list[j]
    print(f"Room {name}:")
    
    if sum(room_list[name]) == 0:
        print("Not available")
        
    else:
        result = []
        start = -1
        for i in range(9, 18):
            if room_list[name][i] == 1:
                if start == -1:
                    start = i
            elif room_list[name][i] == 0:
                if start != -1:
                    result.append(str(start).zfill(2) + "-" + str(i).zfill(2))
                    start = -1
        if start != -1:
            result.append(str(start).zfill(2) + "-" + str(i + 1))
        print(f"{len(result)} available:")
        print("\n".join(result))
    
    if j + 1 != len(name_list):
        print("-----")
        
