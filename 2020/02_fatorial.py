x = 1
numero = int(input('Digite um número:'))
fat = numero - 1
if numero >= 0:
    for i in range (1,numero):
        if numero > 0:
            x = numero * fat
            fat = fat - 1
            numero = numero * (-1)
        else:
            x = x * fat
            fat = fat - 1
    print(x)
else:
    print('Error')
