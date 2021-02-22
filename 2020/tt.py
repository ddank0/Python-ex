# def quicksort(lista):
#     if len(lista) <= 1: return lista
#     m = lista[0]
#     return quicksort([i for i in lista if i < m]) + \
#         [i for i in lista if i == m] + \
#             quicksort([i for i in lista if i > m])

# lista = [13,34,5,56,7,8,95,43,45,2,0,5]
# x = quicksort(lista)
# print(x)
# def quick(lista):
#     if lista:
#             inicio = [x for x in lista if x < lista[0]]
#             fim = [x for x in lista if x > lista[0]]
#             if len(inicio) > 1:
#                     inicio = quick(inicio)
#             if len(fim) > 1:
#                     fim = quick(fim)
#             return inicio + [lista[0]] * lista.count(lista[0]) + fim
#     return []

# lista = [13,34,5,56,7,8,95,43,45,2,0,5,0]
# x = quick(lista)
# print(x)

# lista = ["a","f","g","t","h","u"]
# l = lista
# new = []

# for i in range(0,len(l)):
#     print(i)
#     x = min(l)
#     if l[i] != "xxx":
#         l[i] = "xxx"
#     new.append(x)
# print(new)

# lista = ["a","f","g","t","h","u"]

# def qsort(lista): 
#     if len(lista) <= 1:
#         return lista
#     else:
#         return qsort([x for x in lista[1:] if x < lista[0]]) + \
#                [lista[0]] + \
#                qsort([x for x in lista[1:] if x >= lista[0]])


# def quick(lista):  #quicksort otimizado

#     maior = []
#     menor = []
#     igual = []

#     if len(lista) > 1:
#         x = lista[0]

#         for i in lista:
#             if i < x:
#                 menor.append(i)
#             elif i == x:
#                 igual.append(i)
#             elif i > x:
#                 maior.append(i)

#         return quick(menor) + igual + quick(maior) 
#     else: 
#         return lista

# print(qsort(lista))

#Q8 
#Nome: Gabriel Miranda de Oliveira

# 1   Elabore um programa que leia para uma lista o cpf, o nome e o time de futebol de preferência de um grupo indeterminado de pessoas. Esta entrada deve ser validada. O aluno poderá estabelecer um mínimo de 4 dos principais times podendo ser do Rio de Janeiro (flamengo, fluminense,vasco, botafogo) usando ou não abreviatura ou de outro estado/pais que deseja.

# 2  Usando pesquisa binária verifique se um determinado nome se encontra neste grupo de pessoas.

# 3  O programa deverá ser modularizado com no mínimo 3 funções. Estas funções devem ter um objetivo que deve constar de um comentário.

# 4  Na saída devem aparecer os dados lidos e se a pessoa se encontra ou não no grupo. o nome do time de futebol deve aparecer por extenso

# função destinada a ler dados do usuario
def ler():
    lista = []
    while True:
        nom = input(f'\nNome:')
        if nom == '':
            break
        cpf=input(f'\nDigite seu cpf:')
        time = input(f'\nDigite seu time:\n(fla) para FLAMENGO\n(flu) para FLUMINENSE\n(bot) para BOTAFOGO\n(vas) para VASCO\n* ')
        time = extenso(time)
        # criando um registro com nome, cpf e time
        nome = nom + ',' + cpf + ',' + time
        lista.append(nome)
    return lista


def calc(lista):
    # ordenando a lista
    lista.sort()
    # descompactando a lista
    nome = []
    cpf = []
    time = []
    l = []
    for i in lista:
        l = i.split(',') # divide cada membro da lista separado por ,
        nome.append(l[0])# primeiro termo o nome
        cpf.append(l[1])  # o segundo o cpf
        time.append(l[2]) # terceiro termo o time
        
    # efetuando a busca binária do nome proposto
    fim = len(nome) - 1
    inicio = 0
    nomep = input('Nome a procurar:')
    achei = False
    while inicio <= fim and achei == False:
        meio = (inicio+fim)//2
        if nome[meio] == nomep:
            achei = True
        elif nomep < nome[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    
    nomel = nome
    cpfl = cpf
    timel = time

    return achei,nomep,cpf[meio],time[meio],nomel,cpfl,timel

#colocando as siglas dos times em extenso
def extenso(time):

    if time.upper() == 'FLA':
        time = 'Flamengo'
    elif time.upper() == 'FLU':
        time = 'Fluminense'
    elif time.upper() == 'BOT':
        time = 'Botafogo'
    elif time.upper() == 'VAS':
        time = 'Vasco'
    else:
        time = input(f'\nDigite um time válido:\n(fla) para FLAMENGO\n(flu) para FLUMINENSE\n(bot) para BOTAFOGO\n(vas) para VASCO\n* ')
        time = extenso(time)      
    return time

#imprimindo os dados lidos e a informação de busca
def impr(achei,nomep,cp,tim,nomel,cpfl,timel):

    print ('\n{:*^30}'.format('Dados lidos'))

    for i in range(len(nomel)):
        print(f'\nNome: {nomel[i]}\nCPF: {cpfl[i]}\nTime: {timel[i]}')
        
    print ('\n{:*^30}\n'.format('Resultado'))
    if achei:
        print ('Nome: {:^2s} de cpf {:2s} torcedor do {:2s} encontrado '.format(nomep,cp,tim))
    else:
        print ('Nome: {:^2s} não encontrado '.format(nomep))
    return

#programa principal
l=ler()
achei,nomep,cp,tim,nomel,cpfl,timel=calc(l)
impr(achei,nomep,cp,tim,nomel,cpfl,timel)