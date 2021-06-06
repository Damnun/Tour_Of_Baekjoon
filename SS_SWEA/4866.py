open_case = ['(', '{', '[']
close_case = [')', '}', ']']

for N in range(int(input())):
    result = 0
    parity = []
    data = input()
    for i in data:
        if i in open_case:
            parity.append(i)
        elif i in close_case:
            if parity:
                check = parity.pop()
                if open_case.index(check) != close_case.index(i):
                    break

    if not parity:
        print("#{} {}".format(N+1, 1))
