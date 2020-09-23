peso = float(input('peso do boi:'))
maior_p = 0
maior_n = ''
menor_p = 10000000000000
menor_n = ''
geral = 0
while peso > 0:
    num = input('numero do boi:')
    if peso >= maior_p:
        maior_p = peso
        maior_n = num
    if menor_p >= peso:
        menor_p = peso
        menor_n = num 
    peso = float(input('peso do boi:'))
print(f'''maior peso: {maior_p} numero:{maior_n}
menor peso: {menor_p} numero:{menor_n}''')
