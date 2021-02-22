x = input("digite:")
conts = 0
contv = 0
for i in x:
    if i == " ":
        conts += 1
    elif i.upper() == 'A':
        contv += 1
    elif i.upper() == 'E':
        contv += 1
    elif i.upper() == 'I':
        contv += 1
    elif i.upper() == 'O':
        contv += 1
    elif i.upper() == 'U':
        contv += 1
print(f'Quantidade de espaços em branco: {conts}\nQuantidade de vogais: {contv}')