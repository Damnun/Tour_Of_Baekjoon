from collections import Counter
_ = int(input())
n_data = list(map(int, input().split()))
_ = int(input())
m_data = list(map(int, input().split()))

C = Counter(n_data)
print(' '.join(f'{C[m]}' if m in C else '0' for m in m_data))

