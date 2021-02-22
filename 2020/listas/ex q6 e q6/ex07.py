mat = []
tam = int(input("tamanho da matriz quadrada:"))
soma = 0

for i in range(0,tam):
    mat.append(0)
    mat[i] = []
    for j in range(0,tam):
        mat[i].append(int(input(f"elem [{str(i+1)},{str(j+1)}]:")))

for i in range(len(mat)):
    for j in range(len(mat)):
        if (tam - i - 1) == j:
            soma += mat[i][j]
print(soma)


