nota = []
par = []
imp = []
soma = 0
for i in range(0,5):
    nota.append(float(input('nota:')))

for j in range(0,5):
        if nota[j]%2 == 0 :
            soma += nota[j]
        if nota[j] % 2 != 0:
            soma -= nota[j]
print(soma)
print(nota)