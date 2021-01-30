i = 3456
result = (i + int(i / 1000) + int(i % 1000 / 100) + int(i % 1000 % 100 / 10)
                      + int(i % 1000 % 100 % 10))
print(result)
