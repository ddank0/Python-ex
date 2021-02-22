mat = []
tam = int(input("tamanho da matriz quadrada:"))
x = 0
y = 0
for i in range(0,tam):
    mat.append(0)
    mat[i] = []
    for j in range(0,tam):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))

print ('\n{:*^30}\n'.format(' Matriz Lida '))

for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 0 or mat[i][j] == 1 and tam > 1:
            if i == j and mat[i][j] == 1:
                x += 1
            if i != j and mat[i][j] == 0:
                y += 1   
        print (('{:>10d}').format(mat[i][j]),end='')
    print()

if x == tam and y == ((tam**2)-tam):
    print("\n matriz identidade")
else:
    print("\n não é identidade")
     
