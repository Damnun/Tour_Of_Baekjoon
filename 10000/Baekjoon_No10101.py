gak = [int(input()) for _ in range(3)]
gakset = set(gak)

if sum(gak) == 180:
    if len(gakset) == 1:
        print("Equilateral")
    elif len(gakset) == 2:
        print("Isosceles")
    elif len(gakset) == 3:
        print("Scalene")
else:
    print("Error")
