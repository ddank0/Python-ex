lista_int = []

n = int(input('Digite um número inteiro:'))

while n >= 0:
    lista_int.append(n)
    n = int(input('Digite um número inteiro:'))

for i in range(0, len(lista_int)):

    for j in range(i+1, len(lista_int)):

        if lista_int[i] > lista_int[j]:
            cont = lista_int[i]
            lista_int[i] = lista_int[j]
            lista_int[j] = cont

print(lista_int)