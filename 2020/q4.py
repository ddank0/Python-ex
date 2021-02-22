import random
quantidade = int(input("Digite a quantidade de números desejados:"))
for j in range(0,quantidade):
    x = random.randint(10000,999999)
    y = str(x)
    i2 = ""
    soma = 0
    flag = 0
    for i in y:
        if i == i2:
            print(f"Número: {y} número inválido")
            flag = -1
            break
        i2 = i
    if flag != -1:
        for i in y:
            z = int(i)
            soma += z
    if soma%2 != 0 and flag != -1:
        print(f"Número: {y} número inválido")
        flag = -1
    if y[0] == y[5] and flag != -1:
        print(f"Número: {y} número inválido")
        flag = -1
    if flag == 0:
        print(f"Número: {y} número válido")

