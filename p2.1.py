def removes (lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    
    return l

def cond (x):
    aux = []
    cont =0 
    for i in x:
        y = x.count(i)
        y = str(y)
        g= str(i)
        aux.append(g + '^' + y)
    lit = removes(aux)
    print(f'''. {lit}''')
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

print(f'''\n. {lista_int} \n''')

z = cond(lista_int)