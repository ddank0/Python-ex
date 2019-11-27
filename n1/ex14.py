soma = 0
cont = 0
notas = [0.0]*5
for i in range(0,5):
    notas[i] = float(input('Nota:'))
    soma = soma + notas[i]
media = soma / 5
for item in range(0,5):
    if notas[item] > media:
        cont = cont +1
print('{} alunos acima da média'.format(cont))
