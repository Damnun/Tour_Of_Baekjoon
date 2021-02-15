expression = input()    # 수식을 입력받을 변수 expression
start_index = 0    # 숫자와 연산자를 구분하는 인덱스
number_array = []    # 입력받은 수식 expression에서 숫자만을 저장하기 위한 리스트
sign_array = []    # 입력받은 수식 expression에서 연산자만을 저장하기 위한 리스트
result = 0    # 결과값을 저장할 변수
operator = ['+', '-']

# 수식에서 숫자와 연산자를 분리하여 각 리스트에 추가
for i in range(len(expression)):
    if expression[i] in operator:
        sign_array.append(expression[i])
        number_array.append(int(expression[start_index:i]))
        start_index = i+1

number_array.append(int(expression[start_index:]))


# 수식이 전부 '+' 일 경우 number_array 값을 전부 더한 값이 result
if sign_array.count('+') == len(sign_array):
    result = sum(number_array)

elif sign_array.count('-') == 1:    # 수식에 '-' 가 한 개 들어 있을 경우
    sign_index = sign_array.index('-')
    result += sum(number_array[0:sign_index+1])
    result += (sum(number_array[sign_index+1:]) * -1)

print(result)
print(sign_array)
print(number_array)
