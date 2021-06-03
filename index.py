case = int(input())
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in range(case):
    data = int(input())
    count = 0
    for i in numbers:
        if data % i == 0 and data // i in numbers and data <= 81:
            count = 1
    if count == 1:
        print(f'#{n+1} Yes')    
    else:
        print(f'#{n+1} No')
