maior_a = 0
menor_a = 10000
cont = 0
cont2 = 0
nome = input('nome:')

while nome != 'fim':
    altura = int(input('altura:'))
    # print('nome:',nome,' altura:',altura)

    if altura >= maior_a:
        maior_a = altura 
        cont += 1

    if altura < menor_a :
        menor_a = altura
        cont2 += 1

    if nome == 'MARIA':
        break
    nome = input('nome:')
    
print('maior altura:',maior_a, 'quantidade de pessoas q a possuem:',cont)
if maior_a != menor_a:
    print('2ª maior altura:',menor_a, 'quantidade de pessoas q a possuem:',cont2)

    
    


