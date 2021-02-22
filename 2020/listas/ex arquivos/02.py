# arquivo texto gravar uma qtd indeterminada de nomes
# modulo le e grava
def legrava():
    while True:
        nome=input('digite o nome ')
        if nome == '': break
        arq.write(nome+'\n') #grava um nome por linha
    return
def impr():
    arq.seek(0) # retorna ao inicio do arquivo
    print ('Nomes gravados')
    nome=arq.readlines()
    print ('arquivo como lista  {}'.format(nome))
    print('\nNomes um por linha\n')
    for n in nome:
        print ('\t',n.rstrip())
# programa principal
import os
os.chdir ("f:/" ) # diretorio corrente E
arq=open('nomes1.txt','w+') # abre para escrita e leitura
legrava()
impr()
arq.close()
