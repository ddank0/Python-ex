def write (x,y,z):
    for i in range(0,y):
        for j in range(0,z):
            print(f'[{x[i][j]:^5}]',end='')
        print()
    return x

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
orig = write(mt,tax,tay)


y = matrix(mt)

print('')
print('Matriz transposta:')
trans = write(y,tax,tay),