mod = 1000000
p = mod // 10 * 15
fibo = [0 for _ in range(p)]
fibo[0], fibo[1] = 0, 1

data = int(input())
for i in range(2, p):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
    fibo[i] %= mod

print(fibo[data%p])

"""
기존 메모이제이션을 사용하는 것 보다 훨씬 큰 수를 요구하는 문제였다
O(n)으로도 해결할 수 없는 문제라 새로운 접근 방식이 필요해 엄청 고민했던 것 같다
찾아보니 수학적으로 피보나치수가 가지는 주기가 있다는걸 알게되었다.
피보나치 수를 K로 나눈 나머지는 항상 주기를 가지게 되는데, 이를 피사노 주기(Pisano Period)라고 한다.
주기의 길이가 P이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다고 한다.
M = 10&K 일 때, k > 2 라면 주기는 항상 15 * 10^K-1이므로 문제에서 주어진 M = 10^6을 이용해 주기는 15 * 10^5으로 구할 수 있다.
프로그래머 할건데 뭐하러 수학을 공부해? 라고 어렸을 땐 늘 생각했었다. 주어진 문제를 다각적으로 이해하고 다양한 해결책을 제시하는 것은
엄청난 논리력과 사고력이 필요하고, 그 기반이 수학이라는걸 새삼 깨닫는 하루하루다. 행렬부터 공학수학 제대로 공부해봐야지.

"""