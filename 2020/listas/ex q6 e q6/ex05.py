sq = int(input("digite o numero de linhas da matriz quadrada:"))
mat = []
cont = 0
for i in range(sq):
    mat.append(0)
    mat[i] = []
    for j in range(sq):
        mat[i].append(int(input(f"elem [{i+1},{j+1}]:")))

print ('\n{:*^30}\n'.format(' Matriz Lida '))
for i in range(sq):
    for j in range(sq):
        if mat[i][j] == 0:
            cont += 1
        else:
            pass
        print (('{:>10d}').format(mat[i][j]),end='')
    print()

print(f"\n quantidade de zeros = {cont}")
