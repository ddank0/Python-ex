n = int(input('quantia a sacar:'))
while n != 0:
    if n >= 50:
        x = n // 50
        n = n % 50
        nota = 'nota'
        if x > 1:
            nota = 'notas'
        print(x ,nota,'de 50')
    if n >= 20:
        x = n // 20
        n = n % 20
        nota = 'nota'
        if x > 1:
            nota = 'notas'
        print(x ,nota,'de 20')
    if n >= 5:
        x = n // 5
        n = n % 5
        nota = 'nota'
        if x > 1:
            nota = 'notas'
        print(x ,nota,'de 5')
    if n >= 1:
        x = n // 1
        n = n % 1
        nota = 'nota'
        if x > 1:
            nota = 'notas'
        print(x ,nota,'de 1')
    n = int(input('quantia a sacar:'))
    
