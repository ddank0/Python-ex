# remove uma informação do arquivo

def grava():
    arq=open('prog8.txt','w+')     
    while True:  
        nome=input('Digite um nome --> ')
        if nome =='':break
        arq.write(nome+'\n')
    print ('\n{:*^33s}'.format('Arquivo original'))
    arq.seek(0)
    print ('{:^15s}\n'.format('Nome'))
    for i in arq:
        print(i.rstrip().rjust(10))
    arq.close()
    return                           
def procura():
    erro=False
    arq=open('prog8.txt','r')
    nomes=arq.readlines()
    auxi=open('baux.txt','w+')
    # procura sequencial em arquivo
    nomep=input('Nome a remover ')
    try:
        nomes.remove(nomep+'\n')
        auxi.writelines(nomes)
        
        
    except:  
        print(nomep,'não existe no arquivo')
        erro=True
    
    arq.close() # fecha arq
    auxi.close() # fecha aux
    os.remove('prog8.txt') #apaga prog8.txt
    os.rename('baux.txt','prog8.txt')#renomeia arquivo   
    return erro,nomep
def impr(erro,nomep):
    if erro:
        print('Programa encerrado')
    else:    
        arq=open('prog8.txt','r')     
        print ('\n{:*^33s}'.format('Arquivo alterado'))
        print ('{:^15s}\n'.format('Nome'))
        for i in arq:
            print(i.rstrip().rjust(10))
    return
import os
os.chdir('f:/')
global erro
grava()
erro,nomep=procura()
impr(erro,nomep)