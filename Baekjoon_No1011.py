import math
ans = int(input())
for i in range(ans):
    arr = [1]
    tmp = 2
    a, b = map(int, input().split())
    if (b-a) <= 3:
        print(b-a)
    else:
        n = int(math.sqrt(b-a))
        if b-a == n ** 2:
            print(2*n-1)
        elif n ** 2 < b-a <= n ** 2 + n:
            print(2*n)
        else:
            print(2*n+1)






"""
f(n-1) < n <= f(n)
		    n	차	f(n)
1		    1	0	1
11		    2	1	2
111         3   1   3
121		    4	2	4
1221		6	2	5
12321		9	3	6
123321		12	3	7
1234321		16	4	8
12344321	20	4	9
123454321	25	5	10
1234554321	30	5	11
12345654321	36	6	12

ans = int(input())
for i in range(ans):
    arr = [1]
    tmp = 2
    lresult = rresult = 0
    a, b = map(int, input().split())
    while True:
        arr2 = arr+[]
        arr2.reverse()
        lresult = (sum(arr) * 2 - arr2[0])
        rresult = sum(arr) * 2
        if lresult >= (b-a):
            print(len(arr)*2-1)
            break

        elif rresult >= (b-a):
            print(len(arr)*2)
            break

        arr.append(tmp)
        tmp += 1




f(n-1) < n <= f(n)
		    n	차	f(n)
1		    1	0	1
11		    2	1	2
121		    4	2	3
1221		6	2	4
12321		9	3	5
123321		12	3	6
1234321		16	4	7
12344321	20	4	8
123454321	25	5	9
1234554321	30	5	10
12345654321	36	6	11
"""


"""