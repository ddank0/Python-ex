cont_m = 0
cont_f = 0
soma_m = 0
soma_f = 0
m_salario = 0

idade = int(input('Idade:'))
while idade > 0:
    sexo = input('Sexo:')
    salario = float(input('Salário:'))

    if salario >= m_salario:
        if idade < 30:
            m_salario = salario

    if sexo.upper() == 'F':
        cont_f = cont_f + 1
        soma_f = soma_f + salario

    if sexo.upper() == 'M':
        cont_m = cont_m + 1
        soma_m = soma_m + salario

    idade = int(input('Idade:'))

if cont_m != 0:
    print('Média salarial masculina:',(soma_m/cont_m))

if cont_f != 0:
    print('Média salarial feminina:',(soma_f/cont_f))

print('Maior salário:',m_salario)
