mat = []
lista = []
tam = int(input("tamanho da matriz quadrada:"))
for i in range(tam):
    mat.append(0)
    mat[i] = []
    for j in range(tam):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))
x = int(input("linha para procura:")) - 1

print ('\n{:*^30}\n'.format(' Matriz Lida '))

for i in range(tam):
    for j in range(tam):
        if mat[x][j] not in lista:
            lista.append(mat[x][j])

        print (('{:>10d}').format(mat[i][j]),end='')
    print()

lista.sort()
print(f'\n{lista}')
print(f"\nSegundo menor valor: {lista[1]} ")
