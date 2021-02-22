# gerar 10000 palavras com 5 letras
# o codigo ascii para as letras varia de codigo 97 letra a até 122 letra z
from random import * # importa a biblioteca
from time import *
# aluno: Gabriel Miranda de Oliveira
# algoritmo selecionado: quicksort
#gera palavras
print('Este programa demora. Aguarde........')
a=[] # para o bubble sort
b=[] # para o alg. tradicional
c=[] # para o otimizado 
# atenção não pode usar a=b=c=[] pois qdo altera uma lista as outras ficam iguais
for j in range(10000): #gera 10000 palavras
    palav='' # cria uma palavra vazia
    for i in range(5):
        letra=chr(randint(97,122)) # gera letra aleatoria
        palav+=letra # incorpora a letra gerada a palavra
    a.append(palav)
    b.append(palav)
    c.append(palav)
inicio=time() # captura a hora de inicio
for i in range(9999):
    for j in range(i+1,10000):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
fim=time() # captura a hora de fim
print('O tempo gasto na ordenação bubble sort foi de {:5.3f} segundos'.format(fim-inicio))
# coloque aqui o programa com o algoritmo tradicional
#  vc deve usar a lista b
inicio=time()

def quicksort(lista):  #quicksort tradicinal
    if len(lista) <= 1:
        return lista
    else:
        return quicksort([x for x in lista[1:] if x < lista[0]]) + \
               [lista[0]] + \
               quicksort([x for x in lista[1:] if x >= lista[0]])

x = quicksort(b)

fim=time()
# substitua xxxx pelo nome do algoritmo que vc tiver selecionado
# vc deve usar a lista c
print('O tempo gasto na ordenação quicksort tradicional  foi de {:5.3f} segundos'.format(fim-inicio))
# coloque aqui o programa com o seu algoritmo otimizado
inicio=time()

def quicksort_otimizado(lista):  #quicksort otimizado

    maior = []
    menor = []
    igual = []

    if len(lista) > 1:
        x = lista[0]
        for i in lista:
            if i < x:
                menor.append(i)
            elif i == x:
                igual.append(i)
            elif i > x:
                maior.append(i)

        return quicksort_otimizado(menor) + igual + quicksort_otimizado(maior) 
    else: 
        return lista

x = quicksort_otimizado(c)

fim=time()
print('O tempo gasto na ordenação quicksort otimizada foi de {:5.3f} segundos'.format(fim-inicio))

