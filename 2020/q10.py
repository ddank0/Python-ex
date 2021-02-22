#Q10
# Elabore um programa Python que grave em um arquivo texto um número indeterminado de nomes e salários. 
# Depois leia estes dados e verifique se um determinado nome lido se encontra entre os valores gravados. 
# Exibir o nome e salário caso o nome exista ou mensagem “nome não encontrado ‘. Os salários devem ser validados como número real entre 0 e 100.000,00. 
# Observe que não são permitidos o uso de arquivos binários nem de bibliotecas diferentes daquelas do curso. Fica a livre escolha o método de busca.
# O programa deverá ser modularizado no minimo em duas funções.
# Gabriel Miranda de Oliveira


#leno dados e guardando no arquivo
def ler():
    while True:
        nom = input(f'\nNome: ')
        if nom == '':
            break
        try:
            salario = float(input(f'\nDigite seu salário: '))
        except ValueError:
            salario = float(input(f'\nERROR digite apenas numeros; Digite seu salário: '))
        salario = validar(salario)
        # criando um registro com nome e salario
        nome = nom + ',' + salario+'\n'
        arq.write(nome)
    return
import os

#validando salario
def validar (salario):
    while True:
        if salario < 0 or salario > 100000:
            try:
                salario = float(input(f'\nSeu salario deve estar entre 0 e 100.000; Digite seu salário: '))
            except ValueError:
                salario = float(input(f'\nERROR digite apenas numeros; Digite seu salário: '))
        else:
            break
    salario = str(salario)
    return salario

# ordenando e procurando o nome desejado
def procura():
    arq.seek(0) # retorna ao inicio do arquivo
    lista = arq.readlines()
    lista.sort()
    nome = []
    salario = []
    for i in lista:
        l = i.split(',') # divide cada membro da lista separado por ,
        nome.append(l[0])# primeiro termo o nome
        salario.append(l[1])  # o segundo o salario

    fim = len(nome) - 1
    inicio = 0
    nomep = input(f'\nNome a procurar:')
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
    salariol = salario
    return achei,nomep,salario[meio],nomel,salariol

#imprimindo as informações pedidas
def impr(achei,nomep,sal,nomel,sall):

    print ('\n{:*^30}'.format(' Dados lidos '))

    for i in range(len(nomel)):
        print(f'\nNome: {nomel[i].capitalize()}\nSalario: {sall[i]}\n')
        
    print ('\n{:*^30}\n'.format(' Resultado '))
    if achei:
        print ('Nome: {:^2s}\nSalario: {:2s} '.format(nomep.capitalize(),sal))
    else:
        print ('Nome: {:^2s} não encontrado '.format(nomep.capitalize()))
    return
    
# programa principal

os.chdir ("c:/" ) # diretorio corrente E
arq=open('nomes.txt','w+') # abre para escrita e leitura
ler()
achei,nomep,salario,nomel,salariol = procura()
impr(achei,nomep,salario,nomel,salariol)
arq.close