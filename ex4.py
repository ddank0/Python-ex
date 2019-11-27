id = input('Digite sua idade:')
while id != 'fim':
    id = int(id)
    if id <= 0:
        print('Erro')
    elif 1 <= id <= 3:
        print('Bebe')
    elif 4 <= id <=11:
        print('Criança')
    elif 12 <= id <= 17:
        print ('Teen')
    elif 18 <= id <= 30:
        print('Jovem')
    elif 31 <= id <= 64:
        print('Adulto')
    else:
        print('Senior')
    id = input('Digite sua idade:'
               
               
               
               