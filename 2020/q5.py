# Elabore um programa que:

# 1    Gere para uma lista uma quantidade de "n" nomes alfanuméricos ALEATÓRIOS  todos com 7 caracteres cada, cada qual composto de 4 letras  e 3 algarismos. Por exemplo ; AAAA012
# 2    O código ascii para a letra A é 65 e Z é 90.
# 3    Usando bubble sort ou outro algoritmo conhecido classifique os nomes gerados em ordem alfabética da A até Z;
# 4    Imprima os valores na ordem em que forem gerados e depois de ordenados.
# 5    Não pode usar sort(), max(), min() nem outras bibliotecas do python tipo numpy, scipy etc
# 6    Vc deverá colocar comentários com seu nome e explicando a lógica de seu programa

# Q5 GABRIEL MIRANDA DE OLIVEIRA

#IMPORTANDO BIBLIOTECA
import random
#DECLARANDO VARIAVEIS
lista = ""
quantidade = int(input('Quantidade que deseja gerar:'))
lista2 = []
#GERANDO LISTA COM ALGARISMOS ALEATORIOS
for i in range(0, quantidade):
    lista = ""
    for i in range(0, 4):
        lista += chr(random.randint(65,90))
    for i in range(0, 3):
        lista += str(random.randint(0,9))
    lista2.append(lista)
#IMPRIMINDO LISTA NÃO ORDENADA
print('\n{:*^30}'.format(' Lista original '))

for i in lista2:
    print('\n{:>20.7s}'.format(i))
#ORDENANDO LISTA
for i in range(quantidade):
    for j in range(i+1,quantidade):
        if lista2[i] > lista2[j]:
            lista2[i],lista2[j] = lista2[j],lista2[i]
#IMPRIMIDO LISTA ORDENADA
print('\n{:*^30}'.format(' Lista ordenada '))

for i in lista2:
    print('\n{:>20.7s}'.format(i))
