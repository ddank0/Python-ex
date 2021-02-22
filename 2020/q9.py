#Q9
# 1 Crie um programa Python que emita um relatório sobre o histórico escolar dos alunos do Curso de Ciência da Computação.

# 2 O programa deverá ler o nome do aluno, as disciplinas cursadas e as notas obtidas e deverá guardar em um ou vários dicionários/listas a critério do aluno. O programa deverá usar obrigatoriamente dicionário e listas. Inclua comentários com seu nome e o objetivo de cada trecho.

# 3 A nota deve ser validada como um numero real entre 0 e 10.0

# 4 O programa deve ser modularizado em pelo menos duas funções leitura dos dados e emissão do relatório.

# 5 Para cada aluno, deverá ser emitido um relatório com o nome do aluno, as disciplinas cursadas e as notas obtidas.

# Aluno: Gabriel Miranda de Oliveira

# lendo dados e armazenando os mesmmos

def ler():
    alunos = [] 
    materia = [] 
    dicionario = {} 

    while True: 
        aluno = input("Digite seu nome: ")
        if aluno == "":
            return alunos, materia 
        alunos.append(aluno)
        dicionario.clear()

        while True:
            disciplina = input("Digite a disciplina: ")
            if disciplina == "":
                break

            while True:
                try:
                    nota = float(input("Digite sua nota: "))
                except ValueError:
                    nota = float(input("Error, Digite sua nota novamente: "))
                if nota < 0 or nota > 10 :
                    print("ERROR, digite apenas valores entre 0 e 10.")
                else:
                    dicionario[disciplina] = nota
                    break
        materia.append(dicionario.copy())

# imprimindo dados formatados

def imprimir(alunos, materia):

    print(f'{"+="*30}')

    for i in range(len(alunos)):
        print(f'{"--"*30}')
        print(f'\nAluno: {alunos[i]}\n')
        aux = materia[i]
        print(f'Disciplinas Cursadas:\n')
        for key, val in aux.items():
            print(f'\t{key.upper()}: {val}')
        print(f'\n{"--"*30}')

    print(f'\n{"+="*30}')
    return

# Programa principal
alunos, materia = ler()
imprimir(alunos,materia)
