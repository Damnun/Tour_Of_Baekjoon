for i in range(6, 101):
    for j in range(2, 101):
        for k in range(j + 1, 101):
            for l in range(k + 1, 101):
                if i ** 3 == (j ** 3 + k ** 3 + l ** 3):
                    print(f"Cube = {i}, Triple = ({j}, {k}, {l})")
                if i ** 3 < (j ** 3 + k ** 3 + l ** 3):
                    break
