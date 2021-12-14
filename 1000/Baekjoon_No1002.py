import math
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0 and r1 == r2: # 합동
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: # 내외접
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2): # 서로다른 두 점
        print(2)
    else:
        print(0)
