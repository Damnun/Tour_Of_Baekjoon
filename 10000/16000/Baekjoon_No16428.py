# 5분 1분 10초
# 300초 60초 10초
five = 0
one = 0
ten = 0

time = int(input())

five = time // 300
one = time % 300 // 60
ten = time % 300 % 60 // 10
if time % 300 % 60 % 10 != 0:
    print("-1")
else:
    print(five, one, ten)
