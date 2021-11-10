data = input()

if len(data) == 4:
    print("20")
elif data[0] == '1' and data[1] == '0':
    print(10 + int(data[2]))
elif len(data) >= 3 and data[1] == '1' and data[2] == '0':
    print(10 + int(data[0]))
else:
    print(int(data[0]) + int(data[1]))