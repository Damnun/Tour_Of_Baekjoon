data_count = int(input())

for _ in range(data_count):
    data = input()
    result = 0
    for i in range(len(data)):
        if data[i] == '(':
            result += 1
        elif data[i] == ')':
            result -= 1
        if result == -1:
            print("NO")
            break
        elif i == len(data)-1:
            if result == 0:
                print("YES")
                break
            else:
                print("NO")
                break