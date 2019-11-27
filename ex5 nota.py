cont = 0
soma = 0
nome = input('Nome:')
while nome != 'fim':
    sexo = input('Sexo:')
    n1 = float(input('1ª nota:'))
    n2 = float(input('2ªnota:'))
    media = (n1+n2)/2
    if sexo == 'f':
        print('media feminina individual:',media)
    else:
        cont = cont + 1
        soma = soma + media
    nome = input('Nome:')
if cont != 0:
    print('Media masculina total:',(soma/cont))
