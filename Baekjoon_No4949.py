data_one = ['(', '[']
data_two = [']', ')']
data_match = {']': '[', ')': '('}

while True:
    answer = "yes"
    arr = []
    result = []
    data = input().split('.')
    data = data[0]
    if not len(data):
        break
    for i in data:
        if (i in data_one) or (i in data_two):
            arr.append(i)
    data = []
    if not arr:
        print("yes")
        continue
    if arr[0] in data_two:
        print("no")
        continue

    for i in arr:
        if i in data_one:
            data.append(i)
        elif i in data_two:
            if len(data) == 0 or data[len(data) - 1] != data_match[i]:
                answer = "no"
            try:
                data.pop()
            except:
                answer = "no"
    if len(data) != 0:
        answer = "no"
    print(answer)

"""
스택을 이용하여 ( [ 등과 같이 여는 기호는 저장하고
) ] 는 스택의 pop과 비교하는 식으로 괄호 검사를 진행하였다
문제에서 주어진 내용은 입력을 . 으로 구별하고 . 하나만 입력 되었을 때 반복을 종료해야 했는데
이 때문에 너무 많은 변수를 지정하여 사용한 것은 아닌가. 그리고 종료와 배열의 괄호 탐색 후에
불필요한 조건문이 너무 많은 것 같다는 생각이 든다.

arr에 ] ) 와 같이 닫는 문자열이 먼저 들어오게 되면 pop 할 수 있는 data가 없게 되어
에러가 발생한다. 이 부분을 try-except로 풀긴 하였지만 적합하지 않은 방법인 것 같다

모쪼록 정답 처리는 받았지만 내가 평가자라면 높은 점수를 주긴 어려울 것 같다
더 분발하자. 더 깨져보자
"""