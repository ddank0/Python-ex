cx = float(input('informe o peso da caixa:'))
soma = 0
cont = 0
while cont < 5:
    soma += cx 
    cont += 1
    if cont < 5:
        cx = float(input('informe o peso da caixa:'))
if cont >= 5:
    print('caminhão cheio') 
print('peso total:',soma)
