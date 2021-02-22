n = float(input("Digite um numero:"))
maior_n = 0
soma  = 0
cont = 0

while n > 0:
    cont += 1
    soma += n
    if n > maior_n:
        maior_n = n
    x = soma - maior_n
    n = float(input("Digite um numero:"))

if cont < 3:
    print('Não é possivel formar o poligono')
elif maior_n < x:
    print('É possivel formar o poligono')
else:
    print('Não é possivel formar o poligono')
