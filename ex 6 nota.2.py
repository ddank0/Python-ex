cont_m = 0
cont_f = 0
soma_m = 0
soma_f = 0
nome = input('Nome:')
while nome != 'fim':
    sexo = input('Sexo:')
    n1 = float(input('1ª nota:'))
    n2 = float(input('2ª nota:'))
    media = (n1+n2)/2
    if sexo == 'f':
        cont_f = cont_f + 1
        soma_f = soma_f + media
    else:
        cont_m = cont_m + 1
        soma_m = soma_m + media
    nome = input('Nome:')
if cont_f != 0:
    print('Média feminina:',(soma_f/cont_f))
if cont_m != 0:
    print('Média masculina:',(soma_m/cont_m))
    