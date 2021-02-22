mat = []
lista = []
tam = int(input("tamanho da matriz quadrada:"))
for i in range(tam):
    mat.append(0)
    mat[i] = []
    for j in range(tam):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))

print ('\n{:*^30}\n'.format(' Matriz Lida '))

for i in range(tam):
    for j in range(tam):
        if mat[i][j] not in lista:
            lista.append(mat[i][j])
        print (('{:>10d}').format(mat[i][j]),end='')
    print()

lista.sort()
print(lista)
print(f"\nMenor valor: {lista[1]} ")
