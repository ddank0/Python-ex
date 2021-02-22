cont1 = ('','um','dois','três','quatro','cinco',
        'seis','sete','oito','nove','dez','onze',
        'doze','treze','quatorze','quinze',
        'dezeseis','dezesete','dezoito','dezenove') 
cont2 = ('','vinte','trinta','quarenta','cinquenta',
        'sessenta','setenta','oitenta','noventa')

num = int(input('digite um numero:'))
while num > 0:
    if num < 0 or num > 99:
        print('Numero não suportado')
    elif num == 0:
        print('zero') 
    elif num >= 0 and num < 20:
        print(cont1[num])
    else:
        nums = str(num)
        x = int(nums[0]) - 1
        y = int(nums[1])
        if num % 10 == 0:
            print(cont2[x])
        else:
            print(f'{cont2[x]} e {cont1[y]}')
    num = int(input('digite um numero:'))
