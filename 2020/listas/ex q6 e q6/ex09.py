mat = []
tam = int(input("tamanho da matriz quadrada:"))
ident = []
for i in range(0,tam):
    mat.append(0)
    mat[i] = []
    for j in range(0,tam):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))

print ('\n{:*^30}\n'.format(' Matriz original '))

for i in range(tam):
    ident.append(0)
    ident[i] = []
    for j in range(tam):
        ident[i].append(mat[j][i])

        print (('{:>10d}').format(mat[i][j]),end='')
    print() 

print ('\n{:*^30}\n'.format(' Matriz transposta '))

for i in range(tam):
    for j in range(tam):
        print (('{:>10d}').format(ident[i][j]),end='')
    print()
