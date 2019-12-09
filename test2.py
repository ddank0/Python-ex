def cond (x):
    aux = []
    aux2 = []
    cont =0 
    for i in x:
        y = x.count(i)
        y = str(y)
        g= str(i)
        aux.append(g + '^' + y)
    
    print(aux)
    return aux

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

z = cond(lista_int)