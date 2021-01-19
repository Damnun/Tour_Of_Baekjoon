a = int(input())
index = 1
stack = 1

while (a - stack) > 0:
    print("stack : ", stack)
    stack += 6
    index += 1
print(stack/6)
