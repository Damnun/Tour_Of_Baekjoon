loop = int(input())

for _ in range(loop):
    name, count = input().split()
    count = int(count)

    if 97 <= count <= 100:
        print(name, "A+")
    elif 90 <= count <= 96:
        print(name, "A")
    elif 87 <= count <= 89:
        print(name, "B+")
    elif 80 <= count <= 86:
        print(name, "B")
    elif 77 <= count <= 79:
        print(name, "C+")
    elif 70 <= count <= 76:
        print(name, "C")
    elif 67 <= count <= 69:
        print(name, "D+")
    elif 60 <= count <= 66:
        print(name, "D")
    elif 0 <= count <= 59:
        print(name, "F")
