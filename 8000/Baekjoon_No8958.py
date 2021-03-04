case_amount = int(input())
case = []

for i in range(case_amount):
    ans = input()
    case.append(ans)

current_score = 1
my_score = 0


for i in range(len(case)):
    for index in case[i]:
        if index == 'O':
            my_score += current_score
            current_score += 1

        else:
            current_score = 1

    print(my_score)
    current_score = 1
    my_score = 0
