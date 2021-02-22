mat = []
#quantidade de linhas
for i in range(0,2):
    mat.append(0)
    mat[i] = []
#quantidade de colunas
    for j in range(0,2):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))
        # ou mat[i].append([])
        #    mat[i][j] = int(input("elem:"))

#print matriz em forma de tabela
print ('\n{:*^30}\n'.format(' Matriz Lida '))
for i in range(len(mat[i])):
    for j in range(len(mat[j])):
        print (('\033[31m{:>10d}').format(mat[i][j]),end='')
    print()
