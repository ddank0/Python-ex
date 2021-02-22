mat1 = []
mat2 = []
mat_soma = []
linhas = int(input("quantidade de linhas:"))
colunas = int(input("quantidade de colunas:"))
ident = []
for i in range(linhas):
    mat1.append(0)
    mat2.append(0)
    mat1[i] = []
    mat2[i] = []
    for j in range(colunas):
        mat1[i].append(int(input(f"1ª matriz elem [{str(i+1)},{str(j+1)}]:")))
        mat2[i].append(int(input(f"2ª matriz elem [{str(i+1)},{str(j+1)}]:")))

print ('\n{:*^30}\n'.format(' Primeira Matriz '))

for i in range(linhas):
    mat_soma.append(0)
    mat_soma[i] = []
    for j in range(colunas):
        mat_soma[i].append(mat1[i][j] + mat2[i][j])

        print (('{:>10d}').format(mat1[i][j]),end='')
    print()

print ('\n{:*^30}\n'.format(' Segunda Matriz '))
for i in range(linhas):
    for j in range(colunas):
        print (('{:>10d}').format(mat2[i][j]),end='')
    print()

print ('\n{:*^30}\n'.format(' Segunda Matriz '))
for i in range(linhas):
    for j in range(colunas):
        print (('{:>10d}').format(mat_soma[i][j]),end='')
    print()