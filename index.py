grade = input()
grade = int(grade)

while True:
    if grade < 0 or grade > 100:
        grade = input()
        grade = int(grade)
    else:
        break

if grade >= 90:
    print('A')

elif grade < 90 and grade >= 80:
    print('B')

elif grade < 80 and grade >= 70:
    print('C')

elif grade < 70 and grade >= 60:
    print('D')

else:
    print('F')
