from random import choice
n = input('Nome:')
lista = []
while n != 'fim' :
    lista.append(n)
    n = input('Nome:')
print(f'''
{'=-='*25}''')
print('Os sortedos foram:\n')
for i in range (0,6):
     print(f'   . {choice(lista)}')