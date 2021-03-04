search_data = ['[', ']', '(', ')']
while True:
    answer = "yes"
    arr = []
    data = input().split('.')
    data = data[0]
    if len(data) == 0:
        break
    for i in data:
        if i in search_data:
            arr.append(i)
    result = 0
    for i in arr:
        if result < 0:
            answer = "no"
            break
        elif i == '(':
            result += 1
        elif i == ')':
            result -= 1
        elif i == '[':
            result += 100
        elif i == ']':
            result -= 100
    if result != 0:
        answer = "no"
    print(answer)
