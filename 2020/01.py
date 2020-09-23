frenquencia = float(input('Digite a frequencia do aluno:'))
medidaMensal = float(input('Digite a media mensal do aluno:'))
if (frenquencia >= 70):
    if (medidaMensal >= 7):
        print('Aluno aprovado')
    elif (medidaMensal >= 4 and medidaMensal <= 6.9):
        print('Aluno em prova final')
    else:
        print('Aluno reprovado')
else:
    print('Aluno reprovado')


