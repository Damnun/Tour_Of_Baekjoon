numbers = [3, 30, 34, 5, 9]

for i in range(len(numbers)):
    tmp = str(numbers[i])
    for j in range(i + 1, len(numbers)):
        if i == j:
            continue
        tmp += str(numbers[j])
    numbers.append(tmp)
print(numbers)