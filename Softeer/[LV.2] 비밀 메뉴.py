n, m, k = map(int, input().split())
secret = ''.join(input().split(" "))
data = ''.join(input().split(" "))

if secret in data:
    print("secret")
else:
    print("normal")
