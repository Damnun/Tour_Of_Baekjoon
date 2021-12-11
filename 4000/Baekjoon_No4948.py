import math
import sys
input = sys.stdin.readline

start = 1
while True:
    start = int(input())
    if start == 0:
        break
    end = 2 * start
    count = 0

    if start == 1:
        print("1")
        continue

    array = [True for i in range(end + 1)]

    for i in range(2, int(math.sqrt(end)) + 1):
        if array[i]:
            j = 2
            while i * j <= end:
                array[i * j] = False
                j += 1

    for i in range(start + 1, end + 1):
        if array[i]:

            count += 1

    print(count)
