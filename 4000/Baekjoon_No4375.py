while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1
"""
(A+B)%C = ((A%C) + (B%C)) % C
로 나타낼 수 있음.
파이썬에서는 INT형도 일정 자리 수를 넘어가면 int형이 아닌 어떤 큰 수를 저장하기 위한
자료형으로 변환됨, 따라서 %연산자도 O(1)이 아닌 O(N)만큼의 시간이 소요될 수 있음.
이에 맞게 큰 수를 처리할 때 %를 통해 수를 줄일 수 있는데, %법칙을 잘 이용해야한다.
"""
