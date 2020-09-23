idade = int(input('idade:'))
geral = 0
cont = 0
soma = 0
while idade >= 0:
    geral += 1
    soma += idade
    if  21<= idade <= 65:
        cont += 1
    idade = int(input('idade:'))
    
print(f'''idade média: {soma/geral} anos
pessoas entre 21 e 65 anos: {(cont*100)/geral}%''')

    