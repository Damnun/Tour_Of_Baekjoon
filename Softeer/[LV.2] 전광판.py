import sys
input = sys.stdin.readline 

info = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010', 
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}

t = int(input())
for _ in range(t):
    a, b = map(str,input().split())
    result = 0

    a_zero, b_zero = 5-len(a), 5-len(b)
    a = ' ' * a_zero + a
    b = ' ' * b_zero + b

    for i in range(5):
        for j in range(7):
            if(info[a[i]][j] != info[b[i]][j]):
                result += 1           
    print(result)
