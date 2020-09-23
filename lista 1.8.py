n1 = int(input('digite o primeiro número:'))
n2 = int(input('digite o segundo número:'))
soma = 0
if n1 < n2:
    for i in range((n1 + 1),n2):
        if i%4 == 0:
            soma += i
    print(soma)
else:
    print('não é posivel realizar a soma')

    