p1 = float(input('preço do produto:'))
cont = 0
soma = 0
while p1 > 0:
    soma += p1
    cont += 1
    p1 = float(input('preço do produto:'))

print('Total de gastos:',soma)