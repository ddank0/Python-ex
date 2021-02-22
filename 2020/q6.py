# Elabore um programa que:

# 1    Elabore um programa Python que leia uma matriz quadrada de m xm valores inteiros. Usando pesquisa sequencial verificar se um determinado valor digitado pelo usuário se encontra na diagonal principal.
# 2    Exibir a matriz lida sob a forma de tabela e legendas: "Matriz Lida" e "O valor se encontra (ou não) na diagonal principal".
# 3    Não pode usar os métodos index(), count() ou as bibliotecas numpy, scipy ou outra não integrante ao curso.
# 4    Vc deverá colocar comentários com seu nome e explicando a lógica de seu programa

#Q6 GABRIEL MIRANDA DE OLIVEIRA

#DEFININDO VARIAVEIS
mat = []
ident = []
flag = False
#PEGANDO O NUMERO DE LINHAS E COLUNAS DA MATRIZ
tam = int(input("digite o número de linhas da matriz quadrada:"))

#CRIANDO A MATRIZ
for i in range(0,tam):
    mat.append(0)
    mat[i] = []
    for j in range(0,tam):
        mat[i].append(int(input(f"elemento [{str(i+1)},{str(j+1)}]:")))

#PEGANDO O VALOR A SER PROCURADO
valor = int(input("digite o valor que deseja encontrar:"))

#IMPRIMINDO A MATRIZ ORIGINAL E PROCURANDO O VALOR NA DIAGONAL PRINCIPAL
print ('\n{:*^30}\n'.format(' Matriz Lida '))

for i in range(len(mat)):
    for j in range(len(mat)):
        if i == j and mat[i][j] == valor:
            flag = True
        print (('{:>10d}').format(mat[i][j]),end='')
    print()
    
#IMPRIMINDO SE O VALOR ESTÁ OU NÃO NA DIAGONAL
if flag == True:
    print(f"\n  O valor {valor} se encontra na diagonal principal")
else:
    print(f"\n  O valor {valor} não se encontra na diagonal principal")


