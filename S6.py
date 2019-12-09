from random import shuffle
n = input('nome:')
lista = []
while n != 'fim':
    lista.append(n)
    n = input('nome:')

print(f'''\n{lista}\n''')
shuffle(lista)
print(f'''Lista randomizada:\n \n{lista}''')
