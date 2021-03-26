day = int(input())
math = int(input())
korean = int(input())
math_day = int(input())
korean_day = int(input())

if math % math_day == 0:
    math_result = math // math_day
else:
    math_result = math // math_day + 1

if korean % korean_day == 0:
    korean_result = korean // korean_day
else:
    korean_result = korean // korean_day + 1

result = day - max(math_result, korean_result)
print(result)
