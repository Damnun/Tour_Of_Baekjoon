a = int(input())

for i in range(a):
    if i != 0:
        print("")
    for j in range(a-(i+1)):
        print(" ", end='')
    print("*"*(i+1), end='')
