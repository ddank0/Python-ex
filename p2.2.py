def matrix(x):
    aux = []
    for j in range(len(x[0])):
        linha = []
        for i in range(len(x)):
            linha.append(x[i][j])
        aux.append(linha)
    return aux

mt = []
tax = int(input('x:'))
tay = int(input('y:'))
for i in range(0,tax):
    mt.append(0)
    mt[i] = []
    for j in range(0,tay):
        mt[i].append(int(input('elem:')))

print('-='*25)
print('Matriz original:')
for i in range(0,tax):
    for j in range(0,tay):
        print(f'[{mt[i][j]:^5}]',end='')
    print()


y = matrix(mt)

print('')
print('Matriz tranposta:')
for i in range(0,tax):
    for j in range(0,tay):
        print(f'[{y[i][j]:^5}]',end='')
    print()