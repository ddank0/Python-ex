mat = []
for i in range (0,3):
    mat.append(0)
    mat[i] = []
    for j in range (0,3):
        mat[i].append(int(input('N:')))
        mat[i][j] = int(input('N:'))

soma = 0
for i in range(0,3):
    for j in range(0, 3):
        if [i] == [j]:
            soma += mat[i][j]
print('Soma:',soma)

