from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

array = input().split(' ')
array.sort()

for password in combinations(array, l):
    vowel_count = 0
    for i in password:
        if i in vowels:
            vowel_count += 1
    if 1 <= vowel_count <= l - 2:
        print(''.join(password))
        
"""
만들어야 할 암호의 문자 수 L

주어질 문자들의 개수 C

 

즉 C개의 문자들 중에서 L개를 뽑아야 하는데, 조건이 있다

바로 최소 한 개의 모음과 최소 두개의 자음으로 구성되어야 한다. 라는 것

 

따라서 이 문제를 푸는 방법을 생각해보자면

1. C개의 문자에서 L개를 뽑는다 -> 조합 -> itertools의 combinations를 사용

2. 추가 조건을 만족시키기 위해 combinations의 결과값을 if로 걸러준다.

https://universe-lee.tistory.com/5
"""
