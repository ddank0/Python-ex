cont_par = 0
cont_imp = 0
soma = 0
numero = int(input('Digite um número:'))
while numero != 0:
    if numero % 2 == 0:

        cont_par = cont_par + 1
        soma = soma + numero

    if numero % 2 != 0:
        cont_imp = cont_imp + 1

    numero = int(input('Digite um número:'))

print(cont_imp,'números impar ')
print(cont_par,'números par')
if cont_par != 0:
 print('Média números par =',(soma/cont_par))
