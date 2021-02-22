def quicksort(lista):

    maior = []
    menor = []
    igual = []
    metade = len(lista)//2

    if len(lista) > 1:

        x = lista[0]
        for i in range(len(lista)//2):
            print(lista[i])
            if lista[i] < x:
                menor.append(i)
            elif lista[i] == x:
                igual.append(i)
            elif lista[i] > x:
                maior.append(i)

        return quicksort(menor) + igual + quicksort(maior) 
    else: 
        return lista

lista = [0,3,1,2,4,5,6,7,9,55,4,23,45]
print(lista)
x = quicksort(lista)
print(x)
