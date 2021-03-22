import math
loop = int(input())

for _ in range(loop):
    west, east = map(int, input().split())
    result = math.factorial(east) // (math.factorial(east - west) * math.factorial(west))
    print(result)
