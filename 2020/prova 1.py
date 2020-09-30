peso = int(input('peso:'))
maior_p = 0
menor_p = 1000000000
maior_id = 0
menor_id= 0
cont_n = 0
cont_g = 0
cont_o = 0
while peso > 0 :
    raça = input('raça:')
    ide = input('identificação:')
    if peso > maior_p:
        maior_p = peso
        maior_id = ide
    if peso < menor_p:
        menor_p = peso
        menor_id = ide
    if raça == 'N' and peso > 300:
        cont_n += 1
    if raça == 'G' and peso > 300:
        cont_g += 1
    if raça == 'O' and peso > 300:
        cont_o += 1 
    peso = int(input('peso:'))
print('O boi de maior peso pussui:',maior_p,'Kg identificação:',maior_id)
print('O boi de menor peso pussui:',menor_p,'Kg identificação:',menor_id)
print('Bois nelore com mais de 300kg:',cont_n)
print('Bois gir com mais de 300kg:',cont_g)
print('Outros bois com mais de 300kg:',cont_o)



    

