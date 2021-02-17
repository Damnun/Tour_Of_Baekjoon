expression = input().split('-')
result_expression = []
for i in expression:
    tmp = map(int, i.split('+'))
    result_expression.append(sum(tmp))
print(result_expression[0] - sum(result_expression[1:]))